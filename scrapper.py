import argparse
from collections import OrderedDict
import glob
import os
import shutil
from construct import *
from tqdm import tqdm
setglobalstringencoding(None)

ScrapFile = Struct(
               'path'/PascalString(Int32ul),
               'size'/Int32ul,
               'offset'/Int32ul,
               'data'/OnDemandPointer(this.offset,Bytes(this.size)),
               )
DummyFile = Struct(
               'path'/PascalString(Int32ul),
               'size'/Int32ul,
               'offset'/Int32ul,
               )

PackedHeader = Struct(
                      Const(b'BFPK'),
                      Const(b'\0\0\0\0'),
                      'files'/PrefixedArray(Int32ul,ScrapFile),
                    )
DummyHeader = Struct(
                      Const(b'BFPK'),
                      Const(b'\0\0\0\0'),
                      'files'/PrefixedArray(Int32ul,DummyFile),
                    )
parser = argparse.ArgumentParser(description='Unpack and Repack .packed files')
parser.add_argument('-u', '--unpack', action='store_true',
                    help='unpack file to \'extracted\' directory')
parser.add_argument('-r', '--repack', action='store_true',
                    help='repack file from \'extracted\' directory')

parser.add_argument(
    '--reset',
    action='store_true',
    default=False,
    help='restore backup')

parser.add_argument(
    'scrap_dir',
    metavar='Scrapland Directory',
    type=str,
    default=".",
    help='Scrapland installation directory')
options = parser.parse_args()
scrap_dir = os.path.abspath(options.scrap_dir)

if options.reset:
    print('Restoring Backups and removing extracted folder...')
    for packed_file in glob.glob(os.path.join(scrap_dir, '*.packed.bak')):
        outfile = os.path.basename(packed_file)
        orig_filename = outfile[:-4]
        if os.path.isfile(outfile):
            print('deleting', orig_filename)
            os.remove(orig_filename)
            print('moving', outfile, '->', orig_filename)
            shutil.move(outfile, orig_filename)
        target_folder = os.path.join(
            'extracted', os.path.basename(orig_filename))
        print('deleting', target_folder)
        shutil.rmtree(target_folder)
    if os.path.isdir('extracted'):
        input('Press enter to remove rest of extracted folder')
        shutil.rmtree('extracted')
    exit('Done!')

if not (options.unpack or options.repack):
    parser.print_help()
    exit()
pstatus = ''
if options.unpack:
    if os.path.isdir('extracted'):
        print("Removing extracted folder")
        shutil.rmtree('extracted')
    for packed_file in glob.glob(os.path.join(scrap_dir, '*.packed')):
        os.chdir(scrap_dir)
        BN=os.path.basename(packed_file)
        target_folder = os.path.join(
            'extracted', os.path.basename(packed_file))
        os.makedirs(target_folder, exist_ok=True)
        os.chdir(target_folder)
        print('Unpacking {}'.format(os.path.basename(packed_file)))
        with open(packed_file, 'rb') as pkfile:
            data = PackedHeader.parse_stream(pkfile)
            print("Offset:",hex(pkfile.tell()))
            for file in tqdm(data.files,ascii=True):
                folder, filename = os.path.split(file.path)
                if folder:
                    os.makedirs(folder, exist_ok=True)
                with open(file.path, 'wb') as outfile:
                    outfile.write(file.data())
        print('\r' + ' ' * len(pstatus) + '\r', end='', flush=True)
        os.chdir(scrap_dir)

if (options.unpack and options.repack):
    input('Press enter to rebuild *.packed files from folders in \'extracted\' dir...')  # noqa
    pass

def file_gen(files,offset=0):
    for real_path,size,path in files:
        file=dict(
            path=path,
            offset=offset,
            size=size)
        yield file
        offset+=file['size']

def make_header(files,offset=0):
    files_list=list(file_gen(files,offset))
    return DummyHeader.build(dict(files=files_list))

if options.repack:
    for folder in glob.glob(os.path.join(scrap_dir, 'extracted', '*.packed')):
        data=[]
        filename=os.path.join(scrap_dir,os.path.basename(folder))
        for root,folders,files in os.walk(folder):
            for file in sorted(files):
                file=os.path.join(root,file)
                rel_path=bytes(file.replace(folder, '').replace('\\', '/').lstrip('/'), 'windows-1252')
                size=os.stat(file).st_size
                data.append((file,size,rel_path))
        print("Found {} files for {}".format(len(data),filename))
        offset=len(make_header(data))
        print("Writing",filename)
        header=make_header(data,offset)
        with open(filename,"wb") as outfile:
            outfile.write(header)
            for file,size,rel_path in tqdm(data,ascii=True):
                outfile.write(open(file,"rb").read())
print('Done!')
