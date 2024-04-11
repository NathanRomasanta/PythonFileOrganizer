#python script that organizes folder contents into different subfolders

import os
import shutil


def sortFiles( _path ):
    pass


def main():
    
    directory = input("Enter Directory: ")

    if not os.path.exists(directory):
        print('Error: Invalid directory')

    else:
        try:
            os.mkdir(os.path.join(directory, "Texts"))
            os.mkdir(os.path.join(directory, "Videos"))
            os.mkdir(os.path.join(directory, "Music"))
            os.mkdir(os.path.join(directory, "SourceFiles"))
            os.mkdir(os.path.join(directory, "Documents"))
            os.mkdir(os.path.join(directory, "Images"))
            os.mkdir(os.path.join(directory, "Others"))
    
            sortFiles()

        except FileExistsError:
            print("Folders Already Exists!")
            choice = input("Are you sure you want to continue? (y/n): ")

            if choice.lower() == "y":
                sortFiles()
            else:
                exit


if __name__ == "__main__":
    main()