import os
import shutil
import sys

def organize_files(directory):
    for filename in os.listdir(directory):
        if '.DS_Store' in filename:
            continue
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = os.path.splitext(filename)[1][1:]

            file_extension = os.path.join(directory, file_extension)
            
            if not os.path.exists(file_extension):
                os.makedirs(file_extension)
            
            shutil.move(filepath, os.path.join(directory, file_extension, filename))

if __name__ == '__main__':
    path_to_directory = sys.argv[1]
    
    organize_files(path_to_directory)