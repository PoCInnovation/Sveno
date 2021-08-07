import regex
from reactTypes import *
from parser.useRegex import useRegex
from parser.reactEvents import parseReactEvents
from parser.functions import parseFunctions
from parser.props import parseProps
from parser.reactHooks import parseReactHook
from parser.conditions import parseCondition
from parser.algo_html import html_finder
from parser.loops import parseLoop
from svelteImports import addSvelteImports

def parseComponent(component: Component, imports: list, functions: list, css: str) -> Component:
    variables = useRegex("Variable", component.content, Variable)
    html = html_finder(component.content)
    if isinstance(component, ClassComponent):
        html = regex.sub("this.", "", html)
    functions = parseFunctions(component, functions, variables)
    html, variables = parseProps(html, variables)
    html = parseReactEvents(html)
    if len(component.lifeCycle):
        imports.append(addSvelteImports(component))
    html, functions, variables = parseReactHook(component.content, html, functions, variables)
    html = parseCondition(html)
    html = parseLoop(html)
    component = Component(component.name, html, css, imports, variables, functions, component.lifeCycle)
    return component