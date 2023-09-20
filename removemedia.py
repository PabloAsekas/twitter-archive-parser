# Auto-generated using ChatGPT.

import os

# Path to folders A and B
folder_a = 'parser-output/media'
folder_b = 'parser-output/tweets-md'

# Get the list of files in folder A
files_a = os.listdir(folder_a)

# Create a set to store the names of files in A
files_a_set = set(files_a)

# List to store files not found in B
files_not_found = []

# Traverse files in folder B in depth
for current_directory, subdirectories, files in os.walk(folder_b):
    for file_b in files:
        if file_b.endswith('.txt'):
            # Read the content of the text file in B
            with open(os.path.join(current_directory, file_b), 'r') as file:
                content_b = file.read()

            # Search for file names from A in the content of B
            for file_a in files_a_set.copy():
                if file_a in content_b:
                    files_a_set.remove(file_a)

# The files remaining in files_a_set were not found in the text files of B
files_not_found = list(files_a_set)

# Print the files not found
if files_not_found:
    print("Files from A not found in the text files of B:")
    for file in files_not_found:
        print(file)
else:
    print("All files from A were found in the text files of B.")
