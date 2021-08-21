from template import *
from reactTypes import Component, Imports

def addSvelteImports(component: Component) -> str:
    imports = []
    for elem in component.lifeCycle:
        imports.append(elem.kind)
    imports = list(set(imports)) # filter duplicates
    imports = ", ".join(imports)
    return Imports(TEMPLATE_SVELTE_IMPORTS.format(imports=imports), 'svelte')