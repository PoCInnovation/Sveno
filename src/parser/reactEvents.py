import regex
from reactTypes import *

REGEXP = {
    "onEvent": regex.compile(r'(\<[^><]+)(on)([A-Z][^=]*)=(\{(?:[^{}]*|(?4))*\})[^<>]*>')
}

def parseReactEvents(html):
    find = REGEXP["onEvent"].findall(html)
    for element in find:
        begin = element[0] + element[1] + element[2]
        end = element[0] + element[1] + ":" + element[2].lower()
        html = regex.sub(begin, end, html)
    return html