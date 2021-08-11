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
    for index, file in enumerate(files):
        if type(file.content) == UtilsFile:
            file.isUtilsFile = True
            file.newName = file.oldName
            resolvedFiles.append(files[index])
        elif type(file.content) == Component:
            file.newName = file.oldName + '/' + file.content.name
        else:
            file.isFolder = True
            file.newName = file.oldName + '/'
            resolvedFiles.append(file)
            for index, component in enumerate(file.content):
                prependImportsPath(component.imports)
                newSvelteComponent = File(file.oldName, component, file.oldName + '/' + component.name)
                resolvedFiles.append(newSvelteComponent)
    resolveAllImports(resolvedFiles)
    return resolvedFiles
