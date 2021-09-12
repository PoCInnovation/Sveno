import re as regex
from reactTypes import *
from parser.useRegex import useRegex
import numpy as np

REGEXP = {
    "loop": regex.compile(r'\{(.*)\.map.*=>.*(\<.*\>).*\}'),
    "var": regex.compile(r'=\{(.*)\}'),
    "loop2": regex.compile(r'([a-zA-Z1-9]*)\.map\s*\(\(([^\)]*)\)[^=]*=>')
}

def parseProps(html, variables):
    props = useRegex("props", html, None)
    for i in range(len(props)):
        html = regex.sub("props.", "", html)
        variables.append(Variable("export let", props[i], "undefined"))
    return html, variables

def getBalancedElement(content, openElement, closeElement, startCompt):
    compt = startCompt
    pos = 0

    for i,caracter in enumerate(content):
        if (caracter == openElement):
            compt = compt + 1
        if (caracter == closeElement):
            compt = compt - 1
        if (compt == 0):
            break
    content = content[:i]
    return content

def getBalancedPositionElement(content, openElement, closeElement, startCompt):
    compt = startCompt
    pos = 0
    activation = False

    
    print("\nopen = ", openElement, "close = ", closeElement)
    for i, caracter in enumerate(content):
        print(caracter)
        if (activation == False and openElement == caracter):
            activation = True
        if (activation == False):
            continue
        if (caracter == openElement):
            compt = compt + 1
        if (caracter == closeElement):
            compt = compt - 1
        if (compt == 0):
            break
    return i + 1


def parseLoop(html):
    find = REGEXP["loop2"].findall(html)
    full = -1

    print(html)
    for element in find:
        pos =  REGEXP["loop2"].search(html).span()
        if (full == -1):
            full = getBalancedPositionElement(html[pos[0]:], '{', '}', 1)
        else:
            full = getBalancedPositionElement(html[pos[0]:], '(', ')', 0)
        end = getBalancedElement(html[pos[1]:], '(', ')', 1)
        final = "{#each " + element[0] + " as " + element[1] + "}\n"
        final = final + end + "\n{/each}"
        html = html[:pos[0] - 1] + final + html[pos[0] + full:]
        print("\n\nhtml", html)
        break
    
    return html