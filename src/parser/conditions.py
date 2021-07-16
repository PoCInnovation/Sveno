import regex
from reactTypes import *

REGEXP = {
    "ifCondition": regex.compile(r'(\{(.*)&&.*(\<.*\>).*\})'),
}

def parseCondition(html: str) -> str:
    """parseCondition(): tranform react condition syntax into svelte
    styled condition block

    @html: single string of html content."""

    find = REGEXP["ifCondition"].findall(html)

    if (find):
        result = "{#if " + find[0][1] + "}\n" + find[0][2] + "\n{/if}"
        html = regex.sub(REGEXP["ifCondition"], result, html)
    return html