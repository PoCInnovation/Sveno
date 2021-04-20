from utils import listAllFiles
import regex
from parser_test import getHtmlComponents, getImportsComponents, getFunctionComponents
from reactTypes import ClassComponent

REGEXP = {
    "Class Components": regex.compile(r'(class\s(.*)\sextends\sReact\.Component\s(\{[^}{]*+(?:(?3)[^}{]*)*+\}))', regex.MULTILINE),
    "Functionnal Components": regex.compile(r'(function\s(.*)\(.*\)\s(\{[^}{]*+(?:(?1)[^}{]*)*+\})|[const|let].*=\s\(.*\)\s=>\s(?:\{[^}{]*+(?:(?2)[^}{]*)*+\}))', regex.MULTILINE),
    "Imports": regex.compile(r"import\s.*\sfrom\s\'(?!react).*\'"),
    "HTML": regex.compile(r'(return\s*)(\((?:[^)(]+|(?2))*+\))', regex.MULTILINE),
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
    tabComponents = []

    tabComponents.append(getImportsComponents(content))
    tabComponents.append(getHtmlComponents(content))
    return tabComponents
    # return applyType(components, ClassComponent)


def reactToSvelte(content):
    tabComponents = getComponents(content)
    svelteContent = ""

    svelteContent = svelteContent + "<script>"
    for importComponent in tabComponents[0]:
        svelteContent = svelteContent + "\n\t"
        svelteContent = svelteContent + importComponent
    svelteContent = svelteContent + "\n</script>\n"
    svelteContent = svelteContent + tabComponents[1][0]
    svelteContent = svelteContent + "\n<style>\n\n"
    svelteContent = svelteContent + "</style>"
    return (svelteContent)
    # return [getattr(x, "component") for x in components]
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
