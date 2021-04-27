from utils import listAllFiles
import regex
from parser_test import getHtmlComponents, getImportsComponents, getFunctionComponents, getVariableComponents
from reactTypes import ClassComponent
from parsingComponent import parsingComponents

REGEXP = {
    "Class Components": regex.compile(r'(class\s(.*)\sextends\sReact\.Component\s(\{[^}{]*+(?:(?3)[^}{]*)*+\}))', regex.MULTILINE),
    "Functionnal Components": regex.compile(r'(function\s(.*)\(.*\)\s(\{[^}{]*+(?:(?1)[^}{]*)*+\})|[const|let].*=\s\(.*\)\s=>\s(?:\{[^}{]*+(?:(?2)[^}{]*)*+\}))', regex.MULTILINE),
    "Imports": regex.compile(r"import\s.*\sfrom\s\'(?!react).*\'"),
    "HTML": regex.compile(r'(return\s*)(\((?:[^)(]+|(?2))*+\))', regex.MULTILINE),
    "Variable": regex.compile(r'(const|let|var)\s(.*)\s=[^()](.*)', regex.MULTILINE)
}

TEMPLATE = """<script>
    {imports}

    {variables}
</script>

{html}
"""

# Variable = namedtuple("Variable" ,"qualifier name value")
# Component = namedtuple("Component", "component name content")
# Function = namedtuple("Function", "name args content")
# Html = namedtuple("Html", "content tag closingTag")

def applyType(array, struct):
    typeArray = []

    for elem in array:
        [print (x, end="\n-------------\n") for x in elem]
        print (*elem, sep="\n------------\n")
        typeArray.append(struct(*elem))
    return typeArray

def getComponents(content):
    tabComponents = []

    tabComponents.append(getImportsComponents(content))
    tabComponents.append(getVariableComponents(content))
    tabComponents.append(getHtmlComponents(content))
    return tabComponents
    # return applyType(components, ClassComponent)


def reactToSvelte(content):
    tabComponents = getComponents(content)
    return (parsingComponents(tabComponents, TEMPLATE))


def parseCodebase(folderPath):
    reactFiles = listAllFiles(folderPath)
    svelteFiles = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            svelteFiles.append((
                reactFile.replace(".jsx", ".svelte").replace(folderPath + "/", ""),
                reactToSvelte(file.read())))
    return svelteFiles
