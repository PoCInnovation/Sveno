import regex
from reactTypes import *
from parser.useRegex import useRegex

REGEXP = {
    "loop": regex.compile(r'\{.*map.*=>.*\}')
}

def parseProps(html, variables):
    props = useRegex("props", html, None)
    for i in range(len(props)):
        html = regex.sub("props.", "", html)
        variables.append(Variable("export let", props[i], "undefined"))
    return html, variables