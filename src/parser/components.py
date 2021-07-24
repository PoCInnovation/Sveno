import regex
from reactTypes import *
from parser.useRegex import useRegex
from parser.reactEvents import parseReactEvents
from parser.functions import parseFunctions
from parser.props import parseProps
from parser.reactHooks import parseReactHook
from parser.conditions import parseCondition
from parser.initVars import initVars
from svelteImports import addSvelteImports

def parseComponent(component: Component, imports: list, functions: list, css: str) -> Component:
    """parseComponent(): assemble all required elements (imports, worker functions, associated css)
    into a single final component dataclass.

    @component: Base component that will be completed by other elements.
    Can be a Component such as FunctionalComponent or ClassComponent.

    @imports: list of imports found in initial component
    @functions: list of 'classic' functions that are not considered as components.
    @css: simple pure css bloc as a whole string.
    """
    variables = useRegex("Variable", component.content, Variable)
    html = "".join(useRegex("HTML", component.content, None))
    fileImports = imports.copy()
    if isinstance(component, ClassComponent):
        html = regex.sub("this\.", "", html)
        initVars(component, variables)
    functions = parseFunctions(component, functions, variables)
    html, variables = parseProps(html, variables)
    html = parseReactEvents(html)
    if len(component.lifeCycle):
        fileImports.append(addSvelteImports(component))
    html, functions, variables = parseReactHook(component.content, html, functions, variables)
    html = parseCondition(html)
    return Component(component.name, html, css, fileImports, variables, functions, component.lifeCycle)