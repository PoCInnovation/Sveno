import regex
from reactTypes import *
from parserReact import useRegex

REGEXP = {
    "ifCondition": regex.compile(r'(\{(.*)&&.*(\<.*\>).*\})'),
}

def ParseCondition(html):
    find = REGEXP["ifCondition"].findall(html)

    if (find):
        result = "{#if " + find[0][1] + "}\n" + find[0][2] + "\n{/if}"
        html = regex.sub(REGEXP["ifCondition"], result, html)
    return html