import os, argparse, shutil

#list file FUNCTION
def list_file(dir):
    for file in directory:
        print file

#MOVE the file: WILL MOVE ENTIRE DIRECTORY ELSEWHERE!
def move_file_to_dir(dir, dir2):
        shutil.move(dir, dir2)

#copy all files from one directory to another. dir1 is directory to copy from, dir2 is to copy to
def copy_files(dir, dir1, dir2):
    for file in dir:
        file_name = os.path.join(dir1, file)
        if (os.path.isfile(file_name)):
            shutil.copy(file_name, dir2)

#create an archive of a given directory within that directory
def archive_directory(dir, dir1):
    archive_name = os.path.join(dir1, 'archive')
    root_direct = os.path.expanduser(os.path.join(dir1))
    shutil.make_archive(archive_name, 'gztar', root_direct)

#copy all the files in a folder to folders corresponding to their file extension
def copy_based_type(dir, dir1):
    for file in dir:
        file_name = os.path.join(dir1, file)
        if (os.path.isfile(file_name)):
            if '.txt' in file_name:
                text_move_dir = os.path.expanduser(os.path.join('~', 'Documents'))
                shutil.copy(file_name, text_move_dir)
            elif '.jpg' or '.gif' in file_name:
                pic_move_dir = os.path.expanduser(os.path.join('~', 'Pictures'))
                shutil.copy(file_name, pic_move_dir)

#Move files of a given format into a directory. If the directory doesn't exist create it
def move_files(dir, dir1, dir2):
    for file in dir:
        file_name = os.path.join(dir1, file)
        if (os.path.isfile(file_name)):
            if '.txt' in file_name:
                text_dir = os.path.expanduser(os.path.join(dir1, 'Documents'))
                if not os.path.exists(text_dir):
                    os.makedirs(text_dir)
                shutil.move(file_name, text_dir)
            elif '.jpg' or '.gif' in file_name:
                pic_dir = os.path.expanduser(os.path.join(dir1, 'Pictures'))
                if not os.path.exists(pic_dir):
                    os.makedirs(pic_dir)
                shutil.move(file_name, pic_dir)

parser = argparse.ArgumentParser(description="""Organise your
                                files in a given directory based on the options given""")
parser.add_argument("direct", help="The directory you want to search")
parser.add_argument("direct_two", help="Where you want the files to be copied to")
parser.add_argument("-l", "--list", action="store_true", help="List files in the directory")
parser.add_argument("-m", "--move_directory", action="store_true", help="""Move
                    the directory elsewhere, Warnings: can't be moved within itself, will
                    literally move absolutely everything. Do this at your own risk""")
parser.add_argument("-mf", "--move_files", action="store_true", help="""Move all files to
                    generated folders based on the type of files""")
parser.add_argument("-c", "--copy_directory", action="store_true", help="""Copy the
                    entire contents of a given directory""")
parser.add_argument("-ct", "--copy_type", action="store_true", help="""Copy to a directory
                    based on the type of file being copied""")
parser.add_argument("-a", "--archive_dir", action="store_true", help="""
                    Archive the contents of the given directory into the second given directory""")
args = parser.parse_args()
directory = os.listdir(args.direct) #list directory
directory1 = args.direct #for move_directory
directory2 = args.direct_two # also for move_directory

if args.list:
    list_file(directory)
elif args.move_directory:
    move_file_to_dir(directory1, directory2)
elif args.move_files:
    move_files(directory, directory1, directory2)
elif args.copy_directory:
    copy_files(directory, directory1, directory2)
elif args.copy_type:
    copy_based_type(directory, directory1)
elif args.archive_dir:
    archive_directory(directory, directory2)
else:
    print "Don't want to do anything eh? See help (-h)"
