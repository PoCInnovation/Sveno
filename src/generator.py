from os import mkdir, system
import errno
from utils import pathResolver
from reactTypes import File, UtilsFile

def createFolder(filepath: str) -> None:
    try:
        mkdir(filepath)
    except OSError as err:
        if err.errno != errno.EEXIST:
            print('Creation of directory %s failed' % filepath)
            exit(84)

def cleanUp(folder: str) -> None:
    system("npx prettier --write --plugin-search-dir=./ \"" + folder + "**/**/*.svelte\" 1>/dev/null")

def createFile(filepath: str, content: str) -> None:
    try:
        with open(filepath, 'w') as file:
            file.write(content)
    except OSError:
        print('Couldn\'t write to file')

def createTree(folderPath: str, newFolder, files: list):
    newFolder = pathResolver(newFolder)
    createFolder(newFolder)
    filesResolved = []
    for file in files:
        fileResolved = file.replace(folderPath, '')
        if fileResolved[0] == '/':
            fileResolved = fileResolved[1:]
        filesResolved += [fileResolved]
    print('Found the following files to transpile:')
    for file in filesResolved:
        folders = file.split('/')
        path = ""
        folders.pop()
        for elem in folders:
            path += elem + '/'
            createFolder(newFolder + path)
        print(file)

def generateSvelteCodebase(oldFolder: str, newFolder: str, newFiles: list) -> None:
    for newFile in newFiles:
        if type(newFile) == UtilsFile:
            path = pathResolver(newFile.path.replace(oldFolder, newFolder))
            createFile(path + newFile.name, newFile.content)
            continue
        else:
            path = pathResolver(newFile.path.replace(oldFolder, newFolder))
            createFolder(path)
            createFile(path + newFile.name + ".svelte", newFile.content)
    cleanUp(newFolder)