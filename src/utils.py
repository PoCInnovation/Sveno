from os import listdir
from os.path import isfile, join

def listAllFiles(folderPath: str) -> list:
    return [join(folderPath, f) for f in listdir(folderPath) if isfile(join(folderPath, f))]