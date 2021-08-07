import regex
from regex.regex import Regex
from reactTypes import *
from parser.useRegex import useRegex

REGEXP = {
    "loop": regex.compile(r'\{(.*)\.map.*=>.*(\<.*\>).*\}'),
    "var": regex.compile(r'=\{(.*)\}')
}

def parseProps(html, variables):
    props = useRegex("props", html, None)
    for i in range(len(props)):
        html = regex.sub("props.", "", html)
        variables.append(Variable("export let", props[i], "undefined"))
    return html, variables

def parseLoop(html):
    find = REGEXP["loop"].findall(html)

    if (find):
        findVar = regex.sub(REGEXP["var"], "={element}", find[0][1])
        result = "{#each " + find[0][0] + " as element}\n" + findVar + "\n{/each}"
        html = regex.sub(REGEXP["loop"], result, html)
    return html