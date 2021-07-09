import regex
from reactTypes import *
from parserReact import useRegex
from parseReactEvents import parseReactEvents
from parseFunction import parseFunctions
from parseProps import parseProps
from parseReactHook import parseReactHook
from parseCondition import ParseCondition


def parseComponent(component: Component, imports: list, functions: list, css: str) -> Component:
    variables = useRegex("Variable", component.content, Variable)
    html = "".join(useRegex("HTML", component.content, None))
    if isinstance(component, ClassComponent):
        html = regex.sub("this.", "", html)    
    functions = parseFunctions(component, functions, variables)
    html, variables = parseProps(html, variables)
    html = parseReactEvents(html)
    html, functions, variables = parseReactHook(component.content, html, functions, variables)
    html = ParseCondition(html)
    component = Component(component.name, html, css, imports, variables, functions)
    return component