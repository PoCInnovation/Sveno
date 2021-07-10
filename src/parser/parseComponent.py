import regex
from reactTypes import *
from parser.useRegex import useRegex
from parser.parseReactEvents import parseReactEvents
from parser.parseFunction import parseFunctions
from parser.parseProps import parseProps
from parser.parseReactHook import parseReactHook
from parser.parseCondition import parseCondition
from parser.parseLifeCycle import LIFECYCLE_IMPORTS

def parseComponent(component: Component, imports: list, functions: list, css: str) -> Component:
    variables = useRegex("Variable", component.content, Variable)
    html = "".join(useRegex("HTML", component.content, None))
    if isinstance(component, ClassComponent):
        html = regex.sub("this.", "", html)
    functions = parseFunctions(component, functions, variables)
    html, variables = parseProps(html, variables)
    html = parseReactEvents(html)
    if len(component.lifeCycle):
        for elem in component.lifeCycle:
            imports.append(LIFECYCLE_IMPORTS[elem.kind])
    html, functions, variables = parseReactHook(component.content, html, functions, variables)
    html = parseCondition(html)
    component = Component(component.name, html, css, imports, variables, functions, component.lifeCycle)
    return component