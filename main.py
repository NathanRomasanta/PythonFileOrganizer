#python script that organizes folder contents into different subfolders

import os
import shutil


directory = ""

def sortFiles( _path ):
    for filename in os.listdir(_path):
                f = os.path.join(_path, filename)
                new_path = ""
                # checking if it is a file
                if os.path.isfile(f):
                    try: 
                        if f.endswith('.mp3'):
                            new_path = directory + '/Music/'
                            shutil.move(f, new_path)

                        elif f.endswith(".ai") or f.endswith(".psd") or f.endswith(".prproj") or f.endswith(".psb"):
                            new_path = directory + '/SourceFiles/' 
                            shutil.move(f, new_path)

                        elif f.endswith(".mp4"):
                            new_path = directory + '/Videos/' 
                            shutil.move(f, new_path)

                        elif f.endswith(".txt"):
                            new_path = directory + '/Texts/' 
                            shutil.move(f, new_path)

                        elif f.endswith(".docx") or f.endswith(".pdf") or f.endswith(".ppt") or f.endswith(".xlsx"):
                            new_path = directory + '/Documents/' 
                            shutil.move(f, new_path)

                        elif f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".webp") or f.endswith(".jpg"):
                            new_path = directory + '/Images/' 
                            shutil.move(f, new_path)

                        else:
                            new_path = directory + '/Others/' 
                            shutil.move(f, new_path)


                    
                    except Exception as e:
                        print(f"{e}")


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
    
            sortFiles(directory)

        except FileExistsError:
            print("Folders Already Exists!")
            choice = input("Are you sure you want to continue? (y/n): ")

            if choice.lower() == "y":
                sortFiles(directory)
            else:
                exit


if __name__ == "__main__":
    main()