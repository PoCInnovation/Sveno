from os import mkdir, system
import errno
from reactTypes import UtilsFile

def createFolder(filepath: str) -> None:
    try:
        mkdir(filepath)
    except OSError as err:
        if err.errno != errno.EEXIST:
            print('Creation of directory %s failed' % filepath)
            exit(84)

def cleanUp(folder: str) -> None:
    system("npx prettier --write --plugin-search-dir=./ " + folder + "/**/*.svelte 1>/dev/null")

def createFile(filepath: str, content: str) -> None:
    try:
        with open(filepath, 'w') as file:
            file.write(content)
    except OSError:
        print('Couldn\'t write to file')


def generateSvelteCodebase(newFolder: str, newFiles: list) -> None:
    fullPath = ""

    createFolder(newFolder)
    print("Writing new files")
    for newFile in newFiles:
        fullPath = newFolder + '/' + newFile.newName
        if newFile.isFolder:
            createFolder(fullPath)
        elif type(newFile.content) == UtilsFile:
            createFile(fullPath + ".js", newFile.content.toStr())
            print(fullPath + ".js")
        else:
            print(fullPath + ".svelte")
            createFile(fullPath + ".svelte", newFile.content.toStr())
    cleanUp(newFolder)