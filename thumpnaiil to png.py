import os

# Path to your folder
folder_path = r'C:\Users\huzaif khatib\OneDrive\Desktop\thumbsmall'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.thumb19'):
        # Create full old and new file paths
        old_path = os.path.join(folder_path, filename)
        new_filename = filename.replace('.thumb', '.png')
        new_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} → {new_filename}')