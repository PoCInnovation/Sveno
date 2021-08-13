import regex
from reactTypes import *


REGEXP = {
    "Constructor": regex.compile(r'constructor\s*(\(.*\))\s*\{\s*super\s*(.*)\s*;*\s*(this.state\s*=\s*(\{([^}{]*|(?4))*\}));*\s*\}', regex.MULTILINE),
    "Variables": regex.compile(r'(?<var>\S*)\s*:\s*(?<value>(\{(?:[^}{]*|(?3))*\})|(?:.*))', regex.MULTILINE)
}

def initVars(cComponent: ClassComponent, variables: list) -> list:
    constructor = regex.findall(REGEXP["Constructor"], cComponent.content)
    if (len(constructor)):
        initializedVars = regex.findall(REGEXP["Variables"], constructor[0][3])
        for var in initializedVars:
            variables.append(Variable("let", var[0], var[1]))
