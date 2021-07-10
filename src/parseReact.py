from utils import listAllFiles
import regex
from reactTypes import *
from parser.parseCSS import parseCss
from parser.parseFunction import sortFunctionTypes
from parser.useRegex import useRegex
from parser.parseComponent import parseComponent

LIFECYCLE_IMPORTS = {
    "onMount": "import { onMount } from 'svelte'",
    "beforeUpdate": "import { beforeUpdate } from 'svelte'",
    "afterUpdate": "import { afterUpdate } from 'svelte'",
    "onDestroy": "import { onDestroy } from 'svelte'"
}

def parseLifeCycle(cComponents, imports):
    lifeCycle = []
    for component in cComponents:
        lifeCycle = []
        for key, value in LIFECYCLE_IMPORTS.items():
            tmp = useRegex(key, component.content, LifeCycle)
            if len(tmp):
                lifeCycle.append(tmp[0])
                lifeCycle[len(lifeCycle) - 1].kind = key
        component.lifeCycle = lifeCycle
    return lifeCycle


def reactToSvelte(content: str, path: str) -> list:
    content = regex.sub("className", "class", content)
    components = []
    functions = useRegex("Function", content, Function)
    functionnalComponents, normalFunctions = sortFunctionTypes(functions)
    classComponent = useRegex("Class Component", content, ClassComponent)
    imports = useRegex("Import", content, None)
    css = parseCss(content, path)
    lifeCycle = parseLifeCycle(classComponent, imports)
    print(lifeCycle)

    for fc in functionnalComponents:
        components.append(parseComponent(fc, imports, normalFunctions, css))
    for cc in classComponent:
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
