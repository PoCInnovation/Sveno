from os import walk
from os.path import join, splitext

def listAllFiles(folderPath: str, extensions: list = []) -> list:
    files = []

    if len(extensions) == 0:
        files = [join(dp, f) for dp, dn, filenames in walk(folderPath) for f in filenames]
    else:
        files = [join(dp, f) for dp, dn, filenames in walk(folderPath) for f in filenames if splitext(f)[1] in extensions]
    return files

def pathResolver(path: str):
    return path if path.endswith('/') else path + '/'
