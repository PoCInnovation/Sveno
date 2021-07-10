from parser.useRegex import useRegex
from reactTypes import LifeCycle, UseEffect
import regex

LIFECYCLE = ["onMount", "onDestroy", "beforeUpdate", "afterUpdate"]

REGEXP = {
    "return": regex.compile(r'(\breturn\b\s*(?:(?<brackets>\{(?<content1>(?:[^\}\{]*|(?&brackets))*)\})|(?:\(\s*\)\s*=>\s*)(?:\{(?<content2>(?:[^\}\{]*|(?&brackets))*)\})|(?<content3>.*)))', regex.MULTILINE),
    "dependencies": regex.compile(r'\b\w*')
}

def parseUseEffect(fComponents):
    for component in fComponents:
        effect = useRegex("useEffect", component.content, UseEffect)
        if len(effect):
            onDestroy = regex.findall(REGEXP["return"], effect[0].content)
            if (len(onDestroy)):
                onDestroy = onDestroy[0][0]
                effect[0].content = effect[0].content.replace(onDestroy, '')
                effect[0].onDestroy = regex.sub(r'return\s*(\(\s*\)\s*=>\s*)*', '', onDestroy)
            if (len(effect[0].dependencies) == 0 or len(regex.findall(REGEXP["dependencies"], effect[0].dependencies)) == 0):
                effect[0].onMount = effect[0].content
            else:
                effect[0].afterUpdate = effect[0].content
            component.lifeCycle = effect[0].toLifeCycle()

def parseLifeCycle(cComponents, fComponents, imports):
    lifeCycle = []
    for component in cComponents:
        lifeCycle = []
        for value in LIFECYCLE:
            tmp = useRegex(value, component.content, LifeCycle)
            if len(tmp):
                lifeCycle.append(tmp[0])
                lifeCycle[len(lifeCycle) - 1].kind = value
        component.lifeCycle = lifeCycle
    parseUseEffect(fComponents)
