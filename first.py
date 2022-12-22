# this is for reading each directory

import os
import json

# Set the directory path
directory = "images/trex"

# Get a list of all the file names in the directory
files = os.listdir(directory)

# Save the file names as a JSON array
with open("files.json", "w") as f:
  json.dump(files, f)
