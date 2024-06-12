import os

# Define the path to the folder
path = r"\\HULC-NAS\users\Alex\pilot2\Cyclic_inc\Camera1"

# Loop through all the files in the folder
for filename in os.listdir(path):
    if '_' in filename:
        # Split the filename by '_'
        new_name = filename.split('_', 1)[1]
        # Construct the full file paths
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, new_name)
        # Rename the file
        os.rename(old_file, new_file)

print("Files renamed successfully.")

