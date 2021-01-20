use byteorder::{LittleEndian, ReadBytesExt, WriteBytesExt};
use encoding::{all::WINDOWS_1252, EncoderTrap};
use encoding::{DecoderTrap, Encoding};
use std::{
    collections::VecDeque,
    convert::TryInto,
    fs::{self, File},
    io::Seek,
    path::PathBuf,
};

use std::{fs::create_dir_all, io::SeekFrom};
use structopt::{StructOpt, paw};
use std::{
    io::{BufReader, BufWriter, Read, Write},
    path::Path,
};

#[derive(StructOpt)]
#[structopt(about = "Scrapland .packed packer and unpacker")]
enum Args {
    /// Unpack .packed file
    Unpack {
        destination_folder: PathBuf,
        packed_files: Vec<PathBuf>,
    },
    /// Repack .packed file
    Repack {
        input_folder: PathBuf,
        destination_folder: PathBuf
    }
}
#[derive(Debug, PartialEq, Eq)]
struct FileEntry {
    path: String,
    offset: u32,
    size: u32,
}
#[derive(Debug, PartialEq, Eq)]
struct Packed {
    path: PathBuf,
    ext_path: Option<PathBuf>,
    magic: [u8; 4],
    version: [u8; 4],
    files: Vec<FileEntry>,
}

impl Packed {
    fn from_file(filename: &PathBuf) -> std::io::Result<Packed> {
        let mut fh = BufReader::new(File::open(filename)?);
        let magic: [u8; 4] = [fh.read_u8()?, fh.read_u8()?, fh.read_u8()?, fh.read_u8()?];
        let version: [u8; 4] = [fh.read_u8()?, fh.read_u8()?, fh.read_u8()?, fh.read_u8()?];
        println!("Magic: {:?}", magic);
        println!("Version: {:?}", version);
        let num_files = fh.read_u32::<LittleEndian>()?;
        println!("{} files", num_files);
        let mut files: Vec<FileEntry> = Vec::new();
        for _ in 0..num_files {
            let name_len = fh.read_u32::<LittleEndian>()?;
            let mut name = vec![0; name_len as usize];
            fh.read_exact(&mut name)?;
            let size = fh.read_u32::<LittleEndian>()?;
            let offset = fh.read_u32::<LittleEndian>()?;
            let path = WINDOWS_1252.decode(&name, DecoderTrap::Strict).unwrap();
            files.push(FileEntry { path, offset, size });
        }
        Ok(Packed {
            path: filename.to_owned(),
            magic,
            version,
            files,
            ext_path: None,
        })
    }
    fn size(&self) -> (u64, u64) {
        let mut header_size: u64 = 4 * 3; // Magic+Version+Num files
        let mut data_size: u64 = 0;
        for entry in &self.files {
            header_size += 4 * 3; // Name length, Offset, Size
            let path = WINDOWS_1252
                .encode(&entry.path, EncoderTrap::Strict)
                .unwrap();
            let hs: u64 = path.len().try_into().unwrap();
            header_size += hs;
            data_size += entry.size as u64;
        }
        (header_size, data_size)
    }

    fn from_folder(folder: PathBuf) -> std::io::Result<Self> {
        let mut queue = VecDeque::new();
        queue.push_back(folder.clone());
        let mut header = Packed {
            path: PathBuf::new(),
            magic: [0x42, 0x46, 0x50, 0x4B], // BFPK
            version: [0x00, 0x00, 0x00, 0x00],
            files: vec![],
            ext_path: Some(folder.clone()),
        };
        while let Some(dir) = queue.pop_front() {
            for entry in fs::read_dir(dir)? {
                let entry = entry?;
                let path = entry.path();
                if path.is_dir() {
                    queue.push_back(path);
                } else {
                    let size = path.metadata().unwrap().len().try_into().unwrap();
                    header.files.push(FileEntry {
                        path: path
                            .strip_prefix(folder.clone())
                            .unwrap()
                            .to_string_lossy()
                            .replace("\\", "/"),
                        offset: 0,
                        size,
                    });
                }
            }
        }
        let mut offset = header.size().0.try_into().unwrap();
        for entry in header.files.iter_mut() {
            entry.offset = offset;
            offset += entry.size;
        }
        Ok(header)
    }

    fn write(&self, out_path: &PathBuf) -> std::io::Result<()> {
        let base_path = self.ext_path.clone().unwrap();
        let mut outfile = BufWriter::new(File::create(out_path)?);
        outfile.write_all(&self.magic)?;
        outfile.write_all(&self.version)?;
        outfile.write_u32::<LittleEndian>(self.files.len() as u32)?;
        println!("Building header");
        for entry in &self.files {
            let path = WINDOWS_1252
                .encode(&entry.path, EncoderTrap::Strict)
                .unwrap();
            outfile.write_u32::<LittleEndian>(path.len().try_into().unwrap())?;
            outfile.write_all(&path)?;
            outfile.write_u32::<LittleEndian>(entry.size)?;
            outfile.write_u32::<LittleEndian>(entry.offset)?;
        }
        let total = self.files.len();
        for (n, entry) in self.files.iter().enumerate() {
            println!(
                "[{}/{}] Writing: {} (offset: {}, size: {})",
                n + 1,
                total,
                entry.path,
                entry.offset,
                entry.size
            );
            let mut fh = BufReader::new(File::open(base_path.join(&entry.path))?);
            std::io::copy(&mut fh, &mut outfile)?;
        }
        Ok(())
    }

    fn extract(&mut self, ext_folder: &PathBuf) -> std::io::Result<()> {
        let total = self.files.len();
        let ext_folder = ext_folder.join(&Path::new(&self.path).file_name().unwrap());
        println!("Extracting to {}", ext_folder.to_string_lossy());
        let mut fh = File::open(self.path.clone())?;
        for (n, entry) in self.files.iter().enumerate() {
            println!(
                "[{}/{}] Extracting: {} (offset: {}, size: {})",
                n + 1,
                total,
                entry.path,
                entry.offset,
                entry.size
            );
            fh.seek(SeekFrom::Start(entry.offset.try_into().unwrap()))?;
            let mut data = vec![0; entry.size.try_into().unwrap()];
            let path: PathBuf = PathBuf::from(&entry.path);
            let file = Path::new(&ext_folder).join(path);
            fh.read_exact(&mut data)?;
            create_dir_all(file.parent().unwrap())?;
            let mut fh = BufWriter::new(File::create(file)?);
            fh.write_all(&data)?;
        }
        self.ext_path = Some(ext_folder);
        Ok(())
    }
}

#[paw::main]
fn main(args: Args) -> std::io::Result<()> {
    match args {
        Args::Unpack { packed_files, destination_folder } => {
            for packed_file in &packed_files {
                let mut pkd = Packed::from_file(&packed_file)?;
                pkd.extract(&destination_folder)?;
            }
        }
        Args::Repack { input_folder, destination_folder } => {
            Packed::from_folder(input_folder)?.write(&destination_folder)?;
        }
    }
    Ok(())
}
