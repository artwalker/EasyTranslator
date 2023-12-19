import os
import glob
from termcolor import colored

# Get a list of all text files in the book directory
# Linux version
file_list = glob.glob('./book/*.txt')
# Windows version
# file_list = glob.glob('.\\book\\*.txt')

# Sort the files by their numerical prefix
# Linux version
file_list.sort(key=lambda x: int(x.split('_')[0].split('/')[-1]))
# Windows version
# file_list.sort(key=lambda x: int(x.split('_')[0].split('\\')[-1]))

# Use your translation function on each file
for file in file_list:
    # Print the name of the file you're translating
    print(colored(f'Now translating {file}', 'magenta'))
    os.system(f'python easy_translator.py {file}')

# Print a message when you're done
print(colored('All done!', 'magenta'))
