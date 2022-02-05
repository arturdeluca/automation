#Automation of files to certain folder
#Files must start with the numbers 0 to 9 to be directed to certain folder
#Ideal for basic files

import os
import shutil

srcPath = r'\Users\artur\Desktop\all\python_files\\'
dstPath = r'\Users\artur\Desktop\all\python_files\basic_files\\'

list = os.listdir(srcPath)

for files in list:
    source = srcPath + files
    destination = dstPath + files
    if files.startswith('1'):
        shutil.move(source, destination)
    elif files.startswith('2'):
        shutil.move(source, destination)
    elif files.startswith('3'):
        shutil.move(source, destination)
    elif files.startswith('4'):
        shutil.move(source, destination)
    elif files.startswith('5'):
        shutil.move(source, destination)
    elif files.startswith('6'):
        shutil.move(source, destination)
    elif files.startswith('7'):
        shutil.move(source, destination)
    elif files.startswith('8'):
        shutil.move(source, destination)
    elif files.startswith('9'):
        shutil.move(source, destination)
