from reactTypes import *
import regex
from template import *

REGEXP = {
    "ReactDOM.render": regex.compile(r'(\bReactDOM.render\(\s*<(?<component>.+)\/>,\s*(?<target>document\.(?:[^()]*)|(?:[^()]*(\((?:[^()]*+|(?4))*\))))\);?)', regex.MULTILINE)
}


def parseReactDom(content: str) -> str:
    matches = REGEXP["ReactDOM.render"].findall(content)
    for elem in matches:
        # print(elem)
        component = elem[1]
        target = elem[2]
        content = content.replace(elem[0], TEMPLATE_REACT_DOM_RENDER.format(name=component.lower(), component=component, target = target))
        content = content + f'\nexport default {component.lower()};'
        # print(content)
    return content