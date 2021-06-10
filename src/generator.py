from os import mkdir, system
import errno

def createFolder(filepath: str) -> None:
    try:
        mkdir(filepath)
    except OSError as err:
        if err.errno != errno.EEXIST:
            print('Creation of directory %s failed' % filepath)
            exit(84)
        # print('Note: folder \"%s\" already exists' % filepath)

def cleanUp(folder: str) -> None:
    system("npx prettier --write --plugin-search-dir=../tests/svelte/ " + folder + "/**/*.svelte 1>/dev/null")

def createFile(filepath: str, content: str) -> None:
    try:
        with open(filepath, 'w') as file:
            file.write(content)
    except OSError:
        print('Couldn\'t write to file')

def generateSvelteCodebase(newFolder: str, newFiles: list) -> None:
    fullPath = ""

    createFolder(newFolder)
    for newFile in newFiles:
        fullPath = newFolder + '/' + newFile[0]
        createFolder(fullPath)
        for component in newFile[1]:
            createFile(fullPath + '/' + component.name + ".svelte", component.toStr())
    cleanUp(newFolder)