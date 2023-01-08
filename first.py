import os
import json

# Directory path
dir_path = 'images/wood'

# Get the names of all files in the directory
files = os.listdir(dir_path)

# Sort the files by their creation date
files.sort(key=lambda x: os.path.getctime(os.path.join(dir_path, x)))

# Save the sorted list of file names in a JSON file
with open('files.json', 'w') as f:
    json.dump(files, f)