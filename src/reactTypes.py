from dataclasses import dataclass, field
from typing import List
from template import *

@dataclass
class FunctionnalComponent:
    name: str
    args: str
    content: str
    def toStr(self):
        return self.content

@dataclass
class ClassComponent():
    name: str
    content: str
    def toStr(self):
        return self.content

@dataclass
class Variable:
    qualifier: str
    name: str
    value: str
    def toStr(self):
        return TEMPLATE_VARIABLE.format(qualifier=self.qualifier, name=self.name, value=self.value)

@dataclass
class Function:
    name: str
    args: str
    content: str
    def toStr(self):
        return TEMPLATE_FUNCTION.format(qualifier="const", name=self.name, args= self.args, content=self.content)

@dataclass
class NormalFunction:
    prototype: str
    name: str
    args: str
    content: str
    def toStr(self):
        return self.prototype + " " + self.content

@dataclass
class Component:
    name: str
    htmlContent: str
    imports: List[str] = field(default_factory=list)
    variables: List[Variable] = field(default_factory=list)
    functions: List[NormalFunction] = field(default_factory=list)
    def toStr(self):
        imports = "\n\t".join(self.imports)
        variables = "\n\t".join([x.toStr() for x in self.variables])
        functions = "\n\t".join([fc.toStr() for fc in self.functions])
        return TEMPLATE_SVELTE.format(html=self.htmlContent, imports=imports, variables=variables, functions=functions)


matchTab = {
    FunctionnalComponent: [0, 1, 2],
    ClassComponent: [1, 2],
    Variable: [0, 1, 2],
    Function: [0, 1, 2],
    NormalFunction: [0, 1, 2, 3]
}