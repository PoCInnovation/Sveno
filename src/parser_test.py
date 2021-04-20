import string
import regex

REGEXP_TEST = {
    "function": regex.compile(r'(function.*\))', regex.MULTILINE),
    "Imports": regex.compile(r"import.*"),
    "HTML": regex.compile(r'(<(?:[^)(]+|(?1))*+)', regex.MULTILINE),
    "Variable": regex.compile(r'(const|let|var)\s(.*)\s=[^()](.*)', regex.MULTILINE)
}

def getHtmlComponents(content):
    htmlComponents = REGEXP_TEST["HTML"].findall(content)
    return (htmlComponents)

def getImportsComponents(content):
    importsComponents = REGEXP_TEST["Imports"].findall(content)
    return (importsComponents)

def getFunctionComponents(content):
    functionComponents = REGEXP_TEST["function"].findall(content)
    return (functionComponents)