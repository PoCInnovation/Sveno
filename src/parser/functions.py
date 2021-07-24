import regex
from reactTypes import *
from parser.useRegex import useRegex, applyType
from typing import Tuple

REGEXP = {
    "Class Component": regex.compile(r'(class\s+(?<name>[a-zA-Z0-9_-]+)\s+extends\s+(?:React\.)?Component\s*(?<content>\{(?:[^}{]+|(?&content))*+\}))', regex.MULTILINE),
    "Method": regex.compile(r'(?:(?!constructor)(?<name>\b[[:alnum:]]+)(?<params>\((?:[^)(]+|(?&params))*+\))\s*(?<content>\{(?:[^}{]+|(?&content))*+\})|(?<arrow_name>\b[[:alnum:]]+)\s*=\s*(?<arrow_params>\((?:[^)(]+|(?&arrow_params))*+\))\s*=>\s*(?<arrow_content>\{(?:[^}{]+|(?&arrow_content))*+\}))', regex.MULTILINE),
    "Function": regex.compile(r'(?:function\s+(?<name>.*?)(?<params>\((?:[^)(]+|(?&params))*+\))\s*(?<content>\{(?:[^}{]+|(?&content))*+\})|(?:const|let)\s+?(?<arrow_name>.*?)\s*=\s*(?<arrow_params>\((?:[^)(]+|(?&arrow_params))*+\))\s*=>\s*(?<arrow_content>\{(?:[^}{]+|(?&arrow_content))*+\}))', regex.MULTILINE),
    "Import": regex.compile(r'import\s+.+\s+from\s+\'(?!react).+\''),
    "HTML": regex.compile(r'(<(?:[^)(]+|(?1))>)', regex.MULTILINE),
    "Variable": regex.compile(r'(const|let|var)\s+([a-zA-Z0-9_-]+)\s*=\s*([^;\s]+)'),
    "useState": regex.compile(r'(const|let|var)\s+\[\s*([a-zA-Z0-9_-]+)\s*,\s*([a-zA-Z0-9_-]+)\s*\]\s*=\s*(?:React\.)?useState\(\s*(.+)\s*\)', regex.MULTILINE),
    "useEffect": regex.compile(r'(?:React\.)?useEffect\((.+), (\[.\])\)[^;]', regex.MULTILINE),
    "props": regex.compile(r'props\.([A-Za-z0-9_-]+)'),
    "onEvent": regex.compile(r'(\s)(on)(.*=)'),
    "ifCondition": regex.compile(r'(\{(.*)&&.*(\<.*\>).*\})'),
    "loop": regex.compile(r'\{.*map.*=>.*\}')
}

def sortFunctionTypes(functions: list) -> Tuple[list, list]:
    """
    sortFunctionTypes(): separate classic functions from functionnal components.
    returns a tuple of 2 lists: functionnalComponents[], normalFunctions[]

    @functions: a list of Functions that is not sorted
    """

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

def parseFunctions(component: Component, functions: list, variables: list) -> List:
    if isinstance(component, ClassComponent):
        matches = useRegex("Method", component.content, Function)
        print(matches)
        for match in matches:
            if match.name not in ["render", "constructor"]:
                functions += [match]
    functions += useRegex("Function", component.content, Function)
    for func in functions:
        for var in variables:
            if var.name == func.name:
                variables.remove(var)
    return functions