from typing import Tuple
from reactTypes import *
from reactTypes import UtilsFile
import regex

# def prependImportsPath(imports: list):
#     for elem in imports:
#         if elem.fromFile == True:
#             elem.origin = regex.sub(regex.compile(r"^\.\/"), "../", elem.origin)

# def resolveFileImports(file: File, paths):
#     if file.isFolder:
#         return
#     for path in paths:
#         for elem in file.content.imports:
#             componentName = path[1].split('/')
#             componentName = componentName[len(componentName) - 1]
#             if elem.origin == './' + path[0] or elem.origin == '../' + path[0] and elem.imports == componentName:
#                 elem.origin = elem.origin + '/' + componentName

# def resolveAllImports(files: list):
#     paths = []
#     for file in files:
#         print(file.name)
#         if not file.isFolder:
#             paths.append((file.oldName, file.newName))
#     for file in files:
#         resolveFileImports(file, paths)

# def resolveFileDependencies(files: list):
#     resolvedFiles = []
#     for file in files:
#         if type(file) == UtilsFile:
#             print("I am a util file called " + file.name)
#             resolvedFiles.append(file)
#             continue
#         elif type(file.content) == Component:
#             file.newName = file.oldName + '/' + file.content.name
#             for component in file.content:
#                 prependImportsPath(component.imports)
#                 newSvelteComponent = File(file.oldName, component, file.oldName + '/' + component.name)
#                 resolvedFiles.append(newSvelteComponent)
#             resolvedFiles.append(file)
#         else:
#             print("But i wanna go here lol ", file)
#             file.newName = file.oldName + '/'
#     resolveAllImports(resolvedFiles)
#     return resolvedFiles
