from dataclasses import dataclass

@dataclass
class FunctionnalComponent:
    name: str
    prototype: str
    content: str

@dataclass
class ClassComponent:
    name: str
    content: str

@dataclass
class Variable:
    qualifier: str
    name: str
    value: str

@dataclass
class Function:
    prototype: str
    name: str
    args: str
    content: str

