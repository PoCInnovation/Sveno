from utils import listAllFiles
import regex
import numpy as np
from reactTypes import ClassComponent, Variable, matchTab
from template import TEMPLATE_SVELTE

REGEXP = {
    "Class Component": regex.compile(r'(class\s+([a-zA-Z0-9_-]+)\s+extends\s+(?:React\.)?Component\s*({((?>[^{}]+|(?3))*)}))', regex.MULTILINE),
    "Functionnal Component": regex.compile(r'(function\s(.*)\(.*\)\s(\{[^}{]*+(?:(?1)[^}{]*)*+\})|[const|let].*=\s\(.*\)\s=>\s(?:\{[^}{]*+(?:(?2)[^}{]*)*+\}))', regex.MULTILINE),
    "Import": regex.compile(r'import\s+.+\s+from\s+\'(?!react).+\''),
    "HTML": regex.compile(r'(<(?:[^)(]+|(?1))>)', regex.MULTILINE),
    "Variable": regex.compile(r'(const|let|var)\s+([a-zA-Z0-9_-]+)\s*=\s*([^;\s]+)'),
    "useState": regex.compile(r'(const|let|var)\s+\[\s*([a-zA-Z0-9_-]+)\s*,\s*([a-zA-Z0-9_-]+)\s*\]\s*=\s*(?:React\.)?useState\(\s*(.+)\s*\)', regex.MULTILINE),
    "useEffect": regex.compile(r'(?:React\.)?useEffect\((.+), (\[.\])\)[^;]', regex.MULTILINE)
}

def applyType(matches, struct):
    typeArray = []

    for match in matches:
        print(match)
        elem = [np.asarray(match)[index] for index in matchTab[struct]]
        print(elem)
        typeArray.append(struct(*elem))
    return typeArray

def useRegex(names, content, struct):
    matches = []

    for name in names:
        match = REGEXP[name].findall(content)
        if struct != None:
            matches += applyType(match, struct)
        else:
            matches += match
    return matches


def reactToSvelte(content):
    # components = useRegex(["Class Component", "Functionnal Component"], content)
    regex.sub("className", "class", content)
    imports = useRegex(["Import"], content, None)
    globalsVar = useRegex(["Variable"], content, Variable)
    html = useRegex(["HTML"], content, None)

    print("Imports = ", imports)
    print("Variables = ", globalsVar)
    print("Unified variables = ", "\n".join([x.toStr() for x in globalsVar]));
    print("HTML = ", html)

    return TEMPLATE_SVELTE.format(imports="\n".join(imports), variables="\n".join([x.toStr() for x in globalsVar]), html="\n".join(html))

def parseCodebase(folderPath):
    reactFiles = listAllFiles(folderPath)
    svelteFiles = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            svelteFiles.append((
                reactFile.replace(".jsx", ".svelte").replace(folderPath + "/", ""),
                reactToSvelte(file.read())))
    return svelteFiles
