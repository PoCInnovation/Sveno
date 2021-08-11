from typing import Tuple
from reactTypes import *
from reactTypes import UtilsFile
import regex

def prependImportsPath(imports: list):
    for elem in imports:
        if elem.fromFile == True:
            elem.origin = regex.sub(regex.compile(r"^\.\/"), "../", elem.origin)

def resolveFileImports(file: File, paths):
    if file.isFolder:
        return
    for path in paths:
        for elem in file.content.imports:
            componentName = path[1].split('/')
            componentName = componentName[len(componentName) - 1]
            if elem.origin == './' + path[0] or elem.origin == '../' + path[0] and elem.imports == componentName:
                elem.origin = elem.origin + '/' + componentName

def resolveAllImports(files: list):
    paths = []
    for file in files:
        if not file.isFolder:
            paths.append((file.oldName, file.newName))
    for file in files:
        resolveFileImports(file, paths)

def resolveFileDependencies(files: list):
    resolvedFiles = []
    print('\n\n')
    for index, file in enumerate(files):
        # print(type(file.content))
        if type(file.content) == UtilsFile:
            file.isUtilsFile = True
            file.newName = file.oldName
            resolvedFiles.append(files[index])
            # print('new UtilsFile' + file.newName)
        elif type(file.content) == Component:
            file.newName = file.oldName + '/' + file.content.name
        else:
            file.isFolder = True
            file.newName = file.oldName + '/'
            resolvedFiles.append(file)
            for index, component in enumerate(file.content):
                prependImportsPath(component.imports)
                newSvelteComponent = File(file.oldName, component, file.oldName + '/' + component.name)
                print("Folder: " + newSvelteComponent.oldName + "\nfile: " + newSvelteComponent.newName)
                resolvedFiles.append(newSvelteComponent)
    resolveAllImports(resolvedFiles)
    for elem in resolvedFiles:
        if not elem.isFolder:
            print('new name:' + elem.newName)
    print('\n\n\n')
    return resolvedFiles
