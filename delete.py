import  os


# getting the folder path from the user
folder_path = input("Enter folder path:- ")

# checking whether folder exists or not
if os.path.exists(folder_path):

    # checking whether the folder is empty or not
    if len(os.listdir(folder_path)) == 0:
        # removing the file using the os.remove() method
        os.rmdir(folder_path)
    else:
        # messaging saying folder not empty
        print("Folder is not empty")
else:
    # file not found message
    print("File not found in the directory")