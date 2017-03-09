import os, argparse, shutil

#list file FUNCTION
def list_file(dir):
    for file in directory:
        print file

#copy all files in a directory to a given location
def copy_file_to_dir(dir, dir2):
        shutil.move(dir, dir2)

parser = argparse.ArgumentParser(description="""Organise your
                                files in a given directory based on the options given""")
parser.add_argument("direct", help="The directory you want to search")
parser.add_argument("direct_two", help="Where you want the files to be copied to")
parser.add_argument("-l", "--list", action="store_true", help="List files in the directory")
parser.add_argument("-c", "--copy_all", action="store_true", help="Copy all files in the directory to a given directory")
args = parser.parse_args()
directory = os.listdir(args.direct)
directory1 = args.direct
directory2 = args.direct_two

if args.list:
    list_file(directory)
elif args.copy_all:
    copy_file_to_dir(directory1, directory2)

else:
    print "Don't want to do anything eh? See help (-h)"
