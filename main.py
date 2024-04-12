#python script that organizes folder contents into different subfolders

import os
import shutil




def sortFiles(path):


    #creation of the folders
    os.mkdir(os.path.join(path, "Texts"))
    os.mkdir(os.path.join(path, "Videos"))
    os.mkdir(os.path.join(path, "Music"))
    os.mkdir(os.path.join(path, "SourceFiles"))
    os.mkdir(os.path.join(path, "Documents"))
    os.mkdir(os.path.join(path, "Images"))
    os.mkdir(os.path.join(path, "Others"))
    
    #sorting functionk
    for filename in os.listdir(path):
                f = os.path.join(path, filename)

                new_path = ""
                # checking if it is a file
                if os.path.isfile(f):
                    try: 
                        if f.endswith('.mp3'):
                            new_path = path + '\Music'

                            shutil.move(f, new_path)

                        elif f.endswith(".ai") or f.endswith(".psd") or f.endswith(".prproj") or f.endswith(".psb"):
                            new_path = path + '\SourceFiles' 

                            shutil.move(f, new_path)

                        elif f.endswith(".mp4"):
                            new_path = path + '\Videos' 

                            shutil.move(f, new_path)

                        elif f.endswith(".txt"):
                            new_path = path + '\Texts' 

                            shutil.move(f, new_path)

                        elif f.endswith(".docx") or f.endswith(".pdf") or f.endswith(".ppt") or f.endswith(".xlsx"):
                            new_path = path + '\Documents' 

                            shutil.move(f, new_path)

                        elif f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".webp") or f.endswith(".jpg"):
                            new_path = path + '/Images/' 

                            shutil.move(f, new_path)

                        else:
                            new_path = path + '/Others/' 
                            
                            shutil.move(f, new_path)


                    
                    except Exception as e:
                        print(f"{e}")



def test(path):
     for file in  os.listdir(path):
          print(file)
    
def main():
    
    directory = input("Enter Directory: ")

    if not os.path.exists(directory):
        print('Error: Invalid directory')

    
    try:
        sortFiles(directory)

    except FileExistsError:
        print("Folders Already Exists!")
        choice = input("Are you sure you want to continue? (y/n): ")

        if choice.lower() == "y":
               test(directory)
        else:
            exit


if __name__ == "__main__":
    main()