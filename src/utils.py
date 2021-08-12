import os

"""@package docstring
Documentation for this module.

More details.
"""

def listAllFiles(folderPath: str, extensions: list) -> list:
    folderPath = folderPath + 'src/'
    print(folderPath)
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(folderPath) for f in filenames if os.path.splitext(f)[1] in ['.js', '.jsx']]
    print('Found the following files to transpile:')
    for file in files:
        print(file)
    print("")
    return files