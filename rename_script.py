import os
import re

# Specify the path to the folder you want to work with
folder_path = './'  # Change this to the actual folder path

# Define the regex pattern to extract the size
size_pattern = r'(\d{3,4}x\d{2,3})'

# List all files in the folder
file_list = os.listdir(folder_path)

# Filter files to process only certain file types (e.g., .txt files)
file_list = [file for file in file_list if file.endswith('.gif')]
campaing_start = "Milyar-welcome-offer"
campaing_end = "Lang-tr-Prod-WO"

if file_list:
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        
        # Extract the size from the file name using regex
        match = re.search(size_pattern, file_name)
        size = ""
        
        if match:
            size = match.group(1)
        
        # Define the new file name with the extracted size
        new_file_name = f"{campaing_start}_{size}_{campaing_end}.gif"
        print(new_file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file
        os.rename(file_path, new_file_path)
else:
    print('No .gif files found in the folder.')
