from utils import listAllFiles
import regex
import numpy as np
from reactTypes import ClassComponent, Variable, matchTab



REGEXP = {
    "Class Components": regex.compile(r'(class\s+([a-zA-Z0-9_-]+)\s+extends\s+(?:React\.)?Component\s*({((?>[^{}]+|(?3))*)}))', regex.MULTILINE),
    "Functionnal Components": regex.compile(r'(function\s(.*)\(.*\)\s(\{[^}{]*+(?:(?1)[^}{]*)*+\})|[const|let].*=\s\(.*\)\s=>\s(?:\{[^}{]*+(?:(?2)[^}{]*)*+\}))', regex.MULTILINE),
    "Imports": regex.compile(r'import\s+.+\s+from\s+\'(?!react).+\''),
    "HTMLTag": regex.compile(r'<([a-zA-Z0-9]+)\s*((?:\s*[a-zA-Z]+=[^\s]+))\s><\/[a-zA-Z0-9]+>|<([a-zA-Z0-9]+)\s*((?:\s*[a-zA-Z]+=[^\s]+))\s\/>'),
    "Variable": regex.compile(r'(const|let|var)\s+([a-zA-Z0-9_-]+)\s*=\s*([^;\s]+)'),
    "useState": regex.compile(r'(const|let|var)\s+\[\s*([a-zA-Z0-9_-]+)\s*,\s*([a-zA-Z0-9_-]+)\s*\]\s*=\s*(?:React\.)?useState\(\s*(.+)\s*\)', regex.MULTILINE),
    "useEffect": regex.compile(r'(?:React\.)?useEffect\((.+), (\[.\])\)[^;]', regex.MULTILINE)
}

def applyType(matches, struct):
    typeArray = []

    print("Yes")

    for match in matches:
        print(match)
        elem = [np.asarray(match)[index] for index in matchTab[struct]]
        print(elem)
        typeArray.append(struct(*elem))
    return typeArray

def useRegex(name, content, struct):
    components = REGEXP[name].findall(content)
    return applyType(components, struct)


def reactToSvelte(content):
    components = useRegex("Class Components", content, ClassComponent)

    # parseComponents(components)
    variables = useRegex("Variable", content, Variable)
    # buildTemplate()
    print(components)
    print(variables)

    # print("IMPORTS")
    # print(imports)
    # print("COMPONENTS")
    # print(components, end="\n\n")
    # return TEMPLATE.format".format(imports = "", variables = "\n\t".join([variable.toStr() for variable in variables]), functions = "", html = "", components="")

def parseCodebase(folderPath):
    reactFiles = listAllFiles(folderPath)
    svelteFiles = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            svelteFiles.append((
                reactFile.replace(".jsx", ".svelte").replace(folderPath + "/", ""),
                reactToSvelte(file.read())))
    return svelteFiles
