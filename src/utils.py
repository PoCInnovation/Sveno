import os

"""@package docstring
Documentation for this module.

More details.
"""

def listAllFiles(folderPath: str, extensions: list) -> list:
    files = [join(folderPath, f) for f in listdir(folderPath) if isfile(join(folderPath, f)) and (f.endswith(extensions[0]) or f.endswith(extensions[1]))]
    print('Found the following files to transpile:')
    for file in files:
        print(file)
    print("")
    return files