from dataclasses import dataclass, field
from typing import List
from template import *

@dataclass
class FunctionnalComponent:
    name: str
    prototype: str
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
    prototype: str
    name: str
    args: str
    content: str
    def toStr(self):
        return self.prototype + self.content

matchTab = {
    FunctionnalComponent: [1, 2],
    ClassComponent: [1,2],
    Variable: [0, 1, 2],
    Function: [1,2]
}