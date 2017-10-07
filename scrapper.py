import argparse
from collections import OrderedDict
import configparser
import glob
import os
import shutil
from construct import *
from tqdm import tqdm
setglobalstringencoding(None)
def find_file(name):
    global scrap_dir
    for folder in glob.glob(os.path.join(scrap_dir, 'extracted', '*.packed')):
        for root, folders, files in os.walk(folder):
            for filename in files:
                path = os.path.join(root, filename)
                if filename == name:
                    yield path

def get_config(conf_parse, section, var, default=None):
    return conf_parse[section].get(var, default)


def patch_config(path, section, var, value):
    config = configparser.ConfigParser()
    config.read(path)
    if get_config(config, section, var) == value:
        return
    config[section][var] = value
    with open(path, 'w') as conf:
        config.write(conf)
    return True


def enable_debug_console_gui():
    '''enable debug console (GUI)'''
    for path in find_file('m3d.ini'):
        print('Found', path)
        return patch_config(path, 'video', 'ConsolaWnd', 'SI')


def enable_debug_console_txt():
    '''enable debug console (Text Mode)'''
    path = "Test"
    for path in find_file('m3d.ini'):
        print('Found', path)
        return patch_config(path, 'video', 'ConsolaTxt', 'SI')
    print(path)


patches = [
    enable_debug_console_gui,
    enable_debug_console_txt,
]


def yn(prompt, default='n'):
    c = ['y', 'n']
    default = default.lower()
    assert default in c
    c[c.index(default)] = c[c.index(default)].upper()
    prompt += ' ({}) '.format('/'.join(c))
    return (input(prompt) or default).lower()[0] == 'y'

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
                      'files_cnt'/Rebuild(Int32ul,len_(this.files)),
                      'files'/ScrapFile[this.files_cnt],
                      'offset'/Tell,
                    )
DummyHeader = Struct(
                      Const(b'BFPK'),
                      Const(b'\0\0\0\0'),
                      'files_cnt'/Rebuild(Int32ul,len_(this.files)),
                      'files'/DummyFile[this.files_cnt],
                      'offset'/Tell,
                    )
parser = argparse.ArgumentParser(description='Unpack and Repack .packed files')
parser.add_argument('-u', '--unpack', action='store_true',
                    help='unpack file to \'extracted\' directory')
parser.add_argument('-r', '--repack', action='store_true',
                    help='repack file from \'extracted\' directory')
parser.add_argument('-p', '--patch', action='store_true',
                    help='apply a premade patch')

parser.add_argument(
    '--reset',
    action='store_true',
    default=False,
    help='restore backup')

parser.add_argument(
    'scrap_dir',
    metavar='Scrapland Directory',
    type=str,
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

if not (options.unpack or options.repack or options.patch):
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
            print("Offset:",hex(data.offset))
            for file in tqdm(data.files,ascii=True):
                folder, filename = os.path.split(file.path)
                if folder:
                    os.makedirs(folder, exist_ok=True)
                with open(file.path, 'wb') as outfile:
                    outfile.write(file.data())
        print('\r' + ' ' * len(pstatus) + '\r', end='', flush=True)
        os.chdir(scrap_dir)

if (options.unpack and options.repack) and not options.patch:
    #input('Press enter to rebuild *.packed files from folders in \'extracted\' dir...')  # noqa
    pass

if options.patch:
    print()
    print("Enter Nothing to continue")
    for n, patch in enumerate(patches, 1):
        print('{}. {}'.format(n, patch.__doc__.strip()))
    while 1:
        n = input('Patch to apply: ')
        if not n:
            break
        n = int(n) - 1
        if 0 <= n < len(patches):
            res = patches[n]()
            if res is True:
                print('Applied Succesfully!')
            elif res is None:
                print('Already applied.')
            elif res is False:
                print('Error')
            print()

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
