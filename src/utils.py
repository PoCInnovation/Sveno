from os import listdir
from os.path import isfile, join

def listAllFiles(folderPath: str, extensions: list) -> list:
    folderPath = join(folderPath, 'src/')
    files = [join(folderPath, f) for f in listdir(folderPath) if isfile(join(folderPath, f)) and (f.endswith(extensions[0]) or f.endswith(extensions[1]))]
    print('Found the following files to transpile:')
    for file in files:
        print(file)
    print("")
    return files