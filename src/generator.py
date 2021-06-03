from os import mkdir
import errno

def createFolder(filepath):
    try:
        mkdir(filepath)
    except OSError as err:
        if err.errno != errno.EEXIST:
            print('Creation of directory %s failed' % filepath)
            exit(84)
        # print('Note: folder \"%s\" already exists' % filepath)

def createFile(filepath, content):
    try:
        with open(filepath, 'w') as file:
            file.write(content)
    except OSError:
        print('Couldn\'t write to file')

def generateSvelteCodebase(newFolder, newFiles):
    fullPath = ""

    createFolder(newFolder)
    for newFile in newFiles:
        fullPath = newFolder + '/' + newFile[0]
        createFolder(fullPath)
        for component in newFile[1]:
            createFile(fullPath + '/' + component.name + ".svelte", component.toStr())