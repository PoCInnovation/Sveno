import regex
from reactTypes import *
from parserReact import useRegex
import numpy as np
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