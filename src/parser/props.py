import regex
from reactTypes import *
from parser.useRegex import useRegex

def addVariable(name: str, variables: Variable):
    for var in variables:
        if name == var.name:
            var.qualifier = "export let"
            return
    variables.append(Variable("export let", name, "undefined"))



def parseProps(html, variables):
    props = useRegex("props", html, None)
    for i in range(len(props)):
        html = regex.sub("props.", "", html)
        addVariable(props[i], variables)
    return html, variables