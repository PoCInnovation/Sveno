from os import mkdir
import errno

def generateSvelteCodebase(newFolder, newFiles):
    try:
        mkdir(newFolder)
    except OSError as err:
        if err.errno != errno.EEXIST:
            print('Creation of directory %s failed' % newFolder)
            exit(84)
        print('Note: folder \"%s\" already exists' % newFolder)
    try:
        for newFile in newFiles:
            with open(newFolder + '/' + newFile[0], 'w') as file:
                file.write(newFile[1])
    except OSError:
        print('Couldn\'t write to file')