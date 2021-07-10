from parser.useRegex import useRegex
from reactTypes import LifeCycle

LIFECYCLE_IMPORTS = {
    "onMount": "import { onMount } from 'svelte'",
    "beforeUpdate": "import { beforeUpdate } from 'svelte'",
    "afterUpdate": "import { afterUpdate } from 'svelte'",
    "onDestroy": "import { onDestroy } from 'svelte'"
}

def parseLifeCycle(cComponents, imports):
    lifeCycle = []
    for component in cComponents:
        lifeCycle = []
        for key, value in LIFECYCLE_IMPORTS.items():
            tmp = useRegex(key, component.content, LifeCycle)
            if len(tmp):
                lifeCycle.append(tmp[0])
                lifeCycle[len(lifeCycle) - 1].kind = key
        component.lifeCycle = lifeCycle