from reactTypes import Imports
from parser.useRegex import useRegex

def getImports(content: str) -> list:
    imports = useRegex("Import", content, Imports)
    for elem in imports:
        if elem.origin[0] == '.':
            elem.fromFile = True
    return imports