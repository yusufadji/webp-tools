import os

folders = ["orig", "src", "dst"]

for folder in folders:
    folder_path = folder

    file_list = os.listdir(folder_path)

    for file in file_list:
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)

print("Done.")