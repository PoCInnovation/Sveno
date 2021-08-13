import regex
from reactTypes import *
from parser.useRegex import useRegex, applyType
from typing import Tuple

REGEXP = {
    "HTML": regex.compile(r'(<(?:[^)(]+|(?1))>)', regex.MULTILINE)
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
        for match in matches:
            if match.name not in ["render", "constructor"]:
                functions += [match]
    functions += useRegex("Function", component.content, Function)
    for func in functions:
        for var in variables:
            if var.name == func.name:
                variables.remove(var)
    return functions