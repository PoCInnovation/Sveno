from dataclasses import replace
from locale import normalize
from typing import Iterable, Tuple, Union
from utils import listAllFiles
import regex
import numpy as np
from reactTypes import ClassComponent, Variable, matchTab
from template import TEMPLATE_SVELTE
from parsing_css import parseCss
from reactTypes import *

REGEXP = {
    "Class Component": regex.compile(r'(class\s+([a-zA-Z0-9_-]+)\s+extends\s+(?:React\.)?Component\s*({((?>[^{}]+|(?3))*)}))', regex.MULTILINE),
    "Function": regex.compile(r'(?:function\s+(.*?)(\((?:[^)(]+|(?2))*+\))\s*(\{(?:[^}{]+|(?3))*+\})|(?:const|let)\s+?(.*?)\s*=\s*(\((?:[^)(]+|(?5))*+\))\s*=>\s*(\{(?:[^}{]+|(?3))*+\}))', regex.MULTILINE),
    "Import": regex.compile(r'import\s+.+\s+from\s+\'(?!react).+\''),
    "HTML": regex.compile(r'(<(?:[^)(]+|(?1))>)', regex.MULTILINE),
    "Variable": regex.compile(r'(const|let|var)\s+([a-zA-Z0-9_-]+)\s*=\s*([^;\s]+)'),
    "useState": regex.compile(r'(const|let|var)\s+\[\s*([a-zA-Z0-9_-]+)\s*,\s*([a-zA-Z0-9_-]+)\s*\]\s*=\s*(?:React\.)?useState\(\s*(.+)\s*\)', regex.MULTILINE),
    "useEffect": regex.compile(r'(?:React\.)?useEffect\((.+), (\[.\])\)[^;]', regex.MULTILINE),
    "props": regex.compile(r'props\.([A-Za-z0-9_-]+)')
}

def applyType(matches: list, struct: type) -> list:
    typeArray = []

    for match in matches:
        elem = [np.asarray(match)[index] for index in matchTab[struct]]
        typeArray.append(struct(*elem))
    return typeArray

def useRegex(name: str, content: str, struct: type) -> list:
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

def parseComponent(component: Component, imports: list, functions: list, css: str) -> Component:
    variables = useRegex("Variable", component.content, Variable)
    html = "".join(useRegex("HTML", component.content, None))
    if isinstance(component, ClassComponent):
        html = regex.sub("this.", "", html)
    html = regex.sub("onClick={", "on:click={", html)
    props = useRegex("props", html, None)
    functions += useRegex("Function", component.content, Function)
    for func in functions:
        for var in variables:
            if var.name == func.name:
                variables.remove(var)
    for i in range(len(props)):
        html = regex.sub("props.", "", html)
        variables.append(Variable("export let", props[i], "undefined"))
    component = Component(component.name, html, css, imports, variables, functions)
    return component

def sortFunctionTypes(functions: list) -> Tuple[list, list]:
    functionnalComponents = []
    normalFunctions = []
    for fc in functions:
        elem = REGEXP["HTML"].findall(fc.content)
        if len(elem) > 0:
            fc = [fc.name, fc.args, fc.content]
            functionnalComponents.append(fc)
        else:
            fc = ["function "+ fc.name + fc.args, fc.name, fc.args, fc.content]
            normalFunctions.append(fc)
    functionnalComponents = applyType(functionnalComponents, FunctionnalComponent)
    normalFunctions = applyType(normalFunctions, NormalFunction)

    return functionnalComponents, normalFunctions

def reactToSvelte(content: str, path: str) -> list:
    content = regex.sub("className", "class", content)
    components = []
    functions = useRegex("Function", content, Function)
    functionnalComponents, normalFunctions = sortFunctionTypes(functions)
    classComponent = useRegex("Class Component", content, ClassComponent)
    imports = useRegex("Import", content, None)
    css = parseCss(content, path)

    for fc in functionnalComponents:
        components.append(parseComponent(fc, imports, normalFunctions, css))
    for cc in classComponent:
        components.append(parseComponent(cc, imports, normalFunctions, css))
    return components

def parseCodebase(folderPath: str) -> list:
    reactFiles = listAllFiles(folderPath)
    components = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            components.append((
                reactFile.replace(".jsx", "").rsplit('/', 1)[::-1][0],
                reactToSvelte(file.read(), reactFile)
            ))
    return components
