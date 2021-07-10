from utils import listAllFiles
import regex
from reactTypes import *
from parser.css import parseCss
from parser.functions import sortFunctionTypes
from parser.useRegex import useRegex
from parser.components import parseComponent
from parser.lifeCycle import parseLifeCycle


def reactToSvelte(content: str, path: str) -> list:
    content = regex.sub("className", "class", content)
    components = []
    functions = useRegex("Function", content, Function)
    functionnalComponents, normalFunctions = sortFunctionTypes(functions)
    classComponents = useRegex("Class Component", content, ClassComponent)
    imports = useRegex("Import", content, None)
    css = parseCss(content, path)
    parseLifeCycle(classComponents, functionnalComponents, imports)

    for fc in functionnalComponents:
        components.append(parseComponent(fc, imports, normalFunctions, css))
    for cc in classComponents:
        components.append(parseComponent(cc, imports, normalFunctions, css))
    return components

def parseCodebase(folderPath: str) -> list:
    reactFiles = listAllFiles(folderPath, ".jsx")
    components = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            components.append((
                reactFile.replace(".jsx", "").rsplit('/', 1)[::-1][0],
                reactToSvelte(file.read(), reactFile)
            ))
    return components
