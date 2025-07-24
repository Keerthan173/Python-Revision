import os # Allows us to interact with the operating system

location_path = "C:\\Users\\keert\\OneDrive\\Desktop\\test"

if os.path.exists(location_path):
    print("Path exists")
    if os.path.isfile(location_path):
        print("It is a file")
    elif os.path.isdir(location_path):
        print("It is a directory")       
else:
    print("This location does not exists.")