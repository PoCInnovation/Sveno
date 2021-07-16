import regex
from reactTypes import *
from parser.useRegex import useRegex

def parseReactHook(content, html, functions, variables):
    hookParser = r'\s*\((.*)\))'
    state = useRegex("useState", content, None)
    for var in state:
        variables.append(Variable("let", var[1], var[3]))
        hookParser = regex.compile(f'({var[2]}{hookParser}', regex.MULTILINE)
        for func in functions:
            matches = hookParser.findall(func.content)
            for match in matches:
                func.content = func.content.replace(match[0], f'{var[1]} = {match[1]}')
        matches = hookParser.findall(html)
        for match in matches:
            html = html.replace(match[0], f'{var[1]} = {match[1]}')
    return html, functions, variables