from posixpath import splitext
from utils import pathResolver
from regex.regex import split
import regex
from os import path
from reactTypes import *
from parser.css import parseCss
from parser.functions import sortFunctionTypes
from parser.useRegex import useRegex
from parser.components import parseComponent
from parser.lifeCycle import parseLifeCycle
from parser.imports import getImports
from parser.reactDom import parseReactDom

def reactToSvelte(fullPath: str, name: str, content: str) -> list:
    """reactToSvelte(): tranform the content of a react file into a
    list of svelte styled components.
    @content: the content of a react file.
    @path: the relative path of the file, without the extension. Used for
    creating the correct file dependencies in the transpiled codebase
    """
    content = regex.sub("className", "class", content)
    content = parseReactDom(content)
    components = []
    functions = useRegex("Function", content, Function)
    functionnalComponents, normalFunctions = sortFunctionTypes(functions)
    classComponents = useRegex("Class Component", content, ClassComponent)
    imports = getImports(content)
    css = parseCss(content, name)
    parseLifeCycle(classComponents, functionnalComponents, imports)

    for fc in functionnalComponents:
        components.append(parseComponent(fc, imports, normalFunctions, css))
    for cc in classComponents:
        components.append(parseComponent(cc, imports, normalFunctions, css))
    if len(functionnalComponents) == 0 and len(classComponents) == 0:
        components = handleUtilFile(fullPath, content)
    return components

def handleUtilFile(path: str, content: str):
    if not '/' in path:
        return UtilsFile(
            path,
            './',
            content,
            getImports(content)
        )
    filename, oldPath = path.rsplit('/', 1)[::-1]
    return UtilsFile(
        filename,
        pathResolver(oldPath),
        content,
        getImports(content)
    )

def handleSourceFile(path: str, content: str):
    filename, extension = splitext(path.rsplit('/', 1)[::-1][0])
    transcriptedFile = reactToSvelte(path, filename, content)
    componentFiles = []

    if type(transcriptedFile) == UtilsFile:
        transcriptedFile.name = filename + extension
        return [transcriptedFile]
    for component in transcriptedFile:
        componentFiles += [File(
            component.name,
            pathResolver(path.rsplit('/', 1)[::-1][1] + '/' + filename),
            component.toStr()
        )]
    return componentFiles

def parseCodebase(filesInFolder: list) -> list:
    """parseCodebase(): goes through the entire react source directory
    and returns a list of parsed svelte components to write.

    @folderPath: path to the react source folder. React files' extensions
    should be '.jsx' or '.js'
    """
    SOURCE_EXTENSIONS = [".js", ".jsx"]
    files = []

    for file in filesInFolder:
        _, extension = path.splitext(file)
        with open(file, 'r') as fd:
            content = fd.read()
            if extension not in SOURCE_EXTENSIONS:
                files += [handleUtilFile(file, content)]
            else:
                files += handleSourceFile(file, content)
    return files
