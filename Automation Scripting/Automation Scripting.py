import os
import shutil

# Path to the directory you want to organize
directory = r'L:\coder space\organize file sampling'

# Mapping file extensions to folder names
file_type_folders = {
    'Documents': ['.pdf', '.docx', '.txt', '.ppt', '.pptx'],
    'Excel': ['.xls', '.xlsx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
}

# Create folders if they don't exist
for folder in file_type_folders.keys():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to corresponding folders
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_type_folders.items():
            if file_name.lower().endswith(tuple(extensions)):
                destination_folder = os.path.join(directory, folder)
                destination_path = os.path.join(destination_folder, file_name)
                try:
                    shutil.move(file_path, destination_path)
                    moved = True
                    break
                except Exception as e:
                    print(f"Error moving file {file_name}: {e}")
        if not moved:
            print(f"No matching folder for file: {file_name}")

print("Files have been organized successfully!")
