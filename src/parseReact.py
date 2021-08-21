from utils import listAllFiles
import regex
from re import sub as reSub
from reactTypes import *
from parser.css import parseCss
from parser.functions import sortFunctionTypes
from parser.useRegex import useRegex
from parser.components import parseComponent
from parser.lifeCycle import parseLifeCycle
from parser.imports import getImports
from parser.reactDom import parseReactDom


def reactToSvelte(content: str, path: str) -> list:
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
    css = parseCss(content, path)
    parseLifeCycle(classComponents, functionnalComponents, imports)

    for fc in functionnalComponents:
        components.append(parseComponent(fc, imports, normalFunctions, css))
    for cc in classComponents:
        components.append(parseComponent(cc, imports, normalFunctions, css))
    if len(functionnalComponents) == 0 and len(classComponents) == 0:
        content = regex.sub('import\s*.*\s*from\s*.*', '', content)
        print(content)
        components = UtilsFile(content, imports)
    return components

def parseCodebase(folderPath: str) -> list:
    """parseCodebase(): goes through the entire react source directory
    and returns a list of parsed svelte components to write.

    @folderPath: path to the react source folder. React files' extensions
    should be '.jsx'
    """
    reactFiles = listAllFiles(folderPath, [".jsx", ".js"])
    files = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            files.append(File(
                reactFile.replace(".jsx", "").replace(".js", "").rsplit('/', 1)[::-1][0],
                reactToSvelte(file.read(), reactFile)
            ))
    return files
