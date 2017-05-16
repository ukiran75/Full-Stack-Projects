import os

def rename_files():
    # get the files names in the folder
    file_names = os.listdir(r"I:/prank")
    print(file_names)
    saved_path = os.getcwd()
    #changing the current working directory
    os.chdir(r"I:/prank")
    #renaming every file
    for file_name in file_names:
        #Stripping off the numbers from the file names(python3)
        os.rename(file_name,file_name.lstrip("0123456789"))
    os.chdir(saved_path)


rename_files()