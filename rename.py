#!/usr/bin/python3

import os
import sys
import glob

if len(sys.argv) != 2:
    print("Usage: python3 rename.py <new_name>")
    sys.exit(1)

new_name = sys.argv[1].lower()
files = glob.glob('desk/**/*', recursive=True)

for filename in files:
    try:
        if not os.path.isdir(filename):
            print(filename)
            with open(filename, 'r+') as file:
                contents = file.read()
                if 'sunrise' in contents or 'Sunrise' in contents:
                    print('found em!')
                    new_contents = contents.replace('sunrise', new_name)
                    new_contents = new_contents.replace('Sunrise', new_name.capitalize())
                    file.seek(0)
                    file.write(new_contents)
                    file.truncate()
                    file.close()

        if 'sunrise' in filename:
            os.rename(filename, filename.replace('sunrise', new_name))
    except FileNotFoundError:
        pass

print(f"Replacement complete. All instances of 'sunrise' have been replaced with '{new_name}' in files and folders.")
