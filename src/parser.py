from utils import listAllFiles
import regex
from reactTypes import ClassComponent

REGEXP = {
    "Class Components": regex.compile(r'(class\s(.*)\sextends\sReact\.Component\s(\{[^}{]*+(?:(?3)[^}{]*)*+\}))', regex.MULTILINE),
    "Functionnal Components": regex.compile(r'(function\s(.*)\(.*\)\s(\{[^}{]*+(?:(?1)[^}{]*)*+\})|[const|let].*=\s\(.*\)\s=>\s(?:\{[^}{]*+(?:(?2)[^}{]*)*+\}))', regex.MULTILINE),
    "Imports": regex.compile(r'import\s.*\sfrom\s\'(?!react).*\''),
    "HTML": regex.compile(r'<(.*)><\/.*>|<(.*).*\/>'),
    "Variable": regex.compile(r'(const|let|var)\s(.*)\s=[^()](.*)', regex.MULTILINE)
}

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
    components = REGEXP["Class Components"].findall(content)

    return applyType(components, ClassComponent)


def reactToSvelte(content):
    components = getComponents(content)

    return [getattr(x, "component") for x in components]
    # return '\n'.join(variables)
    # print(components)
    # for var in components:
    #     if type(var) is tuple:
    #         components = components + [x for x in var if x != ""]
    #         components.remove(var)
    # print("IMPORTS")
    # print(imports)
    # print("COMPONENTS")
    # print(components, end="\n\n")
#     return """<script>
#     {imports}

#     {variables}

#     {functions}
# </script>

# {html}
# {components}
# """.format(imports = '\n\t'.join(imports), variables = variables, functions = functions, html = html, components='\n'.join(components))

def parseCodebase(folderPath):
    reactFiles = listAllFiles(folderPath)
    svelteFiles = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            svelteFiles.append((
                reactFile.replace(".jsx", ".svelte").replace(folderPath + "/", ""),
                reactToSvelte(file.read())))
    return svelteFiles
