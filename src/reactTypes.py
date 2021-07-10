from dataclasses import dataclass, field
from os import O_NDELAY
from typing import List

from numpy.core.records import array
from template import *

@dataclass
class LifeCycle:
    args: str
    content: str
    kind: str = None
    def toStr(self):
        return TEMPLATE_LIFECYCLE.format(kind=self.kind, args=self.args, content=self.content)

@dataclass
class UseEffect:
    content: str
    dependencies: str
    onDestroy: str = None
    onMount: str = None
    afterUpdate: str = None
    def toLifeCycle(self):
        lifeCycle = []
        if (self.onDestroy != None):
            lifeCycle.append(LifeCycle('()', self.onDestroy, 'onDestroy'))
        if (self.onMount != None):
            lifeCycle.append(LifeCycle('()', self.onMount, 'onMount'))
        if (self.afterUpdate != None):
            lifeCycle.append(LifeCycle('()', self.afterUpdate, 'afterUpdate'))
        return lifeCycle

@dataclass
class FunctionnalComponent:
    name: str
    args: str
    content: str
    lifeCycle: List[LifeCycle] = field(default_factory=list)
    def toStr(self):
        return self.content

@dataclass
class ClassComponent():
    name: str
    content: str
    lifeCycle: list = None
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
    css: str
    imports: List[str] = field(default_factory=list)
    variables: List[Variable] = field(default_factory=list)
    functions: List[NormalFunction] = field(default_factory=list)
    lifeCycle:  List[LifeCycle] = field(default_factory=list)
    def toStr(self):
        imports = "\n\t".join(self.imports)
        variables = "\n\t".join([x.toStr() for x in self.variables])
        functions = "\n\t".join([fc.toStr() for fc in self.functions])
        lc = "\n\t".join([elem.toStr() for elem in self.lifeCycle])
        return TEMPLATE_SVELTE.format(html=self.htmlContent, imports=imports, variables=variables, functions=functions, style=self.css, lifeCycle=lc)


matchTab = {
    FunctionnalComponent: [0, 1, 2],
    ClassComponent: [1, 2],
    Variable: [0, 1, 2],
    Function: [0, 1, 2],
    NormalFunction: [0, 1, 2, 3],
    LifeCycle: [0, 1],
    UseEffect: [0, 1]
}