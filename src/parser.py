from dataclasses import replace
from utils import listAllFiles
import regex
import numpy as np
from reactTypes import *

REGEXP = {
    "Class Component": regex.compile(r'(class\s+([a-zA-Z0-9_-]+)\s+extends\s+(?:React\.)?Component\s*({((?>[^{}]+|(?3))*)}))', regex.MULTILINE),
    "Functionnal Component": regex.compile(r'(?:function\s+(.*?)(\((?:[^)(]+|(?2))*+\))\s*(\{(?:[^}{]+|(?3))*+\})|(?:const|let)\s+?(.*?)\s*=\s*(\((?:[^)(]+|(?5))*+\))\s*=>\s*(\{(?:[^}{]+|(?3))*+\}))', regex.MULTILINE),
    "Import": regex.compile(r'import\s+.+\s+from\s+\'(?!react).+\''),
    "HTML": regex.compile(r'(<(?:[^)(]+|(?1))>)', regex.MULTILINE),
    "Variable": regex.compile(r'(const|let|var)\s+([a-zA-Z0-9_-]+)\s*=\s*([^;\s]+)'),
    "useState": regex.compile(r'(const|let|var)\s+\[\s*([a-zA-Z0-9_-]+)\s*,\s*([a-zA-Z0-9_-]+)\s*\]\s*=\s*(?:React\.)?useState\(\s*(.+)\s*\)', regex.MULTILINE),
    "useEffect": regex.compile(r'(?:React\.)?useEffect\((.+), (\[.\])\)[^;]', regex.MULTILINE),
    "props": regex.compile(r'props\.([A-Za-z0-9_-]+)')
}

def applyType(matches, struct):
    typeArray = []

    for match in matches:
        elem = [np.asarray(match)[index] for index in matchTab[struct]]
        typeArray.append(struct(*elem))
    return typeArray

def useRegex(name, content, struct):
    matches = []

    match = REGEXP[name].findall(content)
    for i in range(len(match)):
        while match[i][0] == '':
            match[i] = match[i][1:]
    if struct != None:
        matches += applyType(match, struct)
    else:
        matches += match
    return matches

def parseComponent(component, imports):
    variables = useRegex("Variable", component.content, Variable)
    html = "".join(useRegex("HTML", component.content, None))
    if isinstance(component, ClassComponent):
        html = regex.sub("this.", "", html)
    props = useRegex("props", html, None)
    for i in range(len(props)):
        html = regex.sub("props.", "", html)
        variables.append(Variable("export let", props[i], "undefined"))
    component = Component(component.name, html, imports, variables)
    return component

def reactToSvelte(content):
    content = regex.sub("className", "class", content)
    components = []
    functionnalComponent = useRegex("Functionnal Component", content, FunctionnalComponent)
    classComponent = useRegex("Class Component", content, ClassComponent)
    imports = useRegex("Import", content, None)

    # print("CLASS COMPONENTS = ", classComponent)
    # print("FUNCTIONNAL COMPONENTS = ", functionnalComponent)

    for fc in functionnalComponent:
        components.append(parseComponent(fc, imports))
    for cc in classComponent:
        components.append(parseComponent(cc, imports))
    return components

def parseCodebase(folderPath):
    reactFiles = listAllFiles(folderPath)
    components = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            components.append((
                reactFile.replace(".jsx", "").rsplit('/', 1)[::-1][0],
                reactToSvelte(file.read())
            ))
    return components
