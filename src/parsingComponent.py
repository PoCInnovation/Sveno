import regex

def concatImports(importComponents):
    str = ""

    for component in importComponents:
        if (component == importComponents[0]):
            str = str + component
        else:
            str = str + "\n    " + component
    return (str)

def concatVariables(variableComponents):
    str = ""

    for component in variableComponents:
        if (component == variableComponents[0]):
            str = str + (component[0] + " " + component[1] + " = " + component[2])
        else:
            str = str + "\n    " + (component[0] + " " + component[1] + " = " + component[2])
    return (str)

def concatHtml(htmlComponents):
    str = ""

    for component in htmlComponents:
        if (component == htmlComponents[0]):
            str = str + component
        else:
            str = str + "\n    " + component
    return (str)

def parsingComponents(tabComponent, template):
    tab = []
    str = ""
    str = template

    tab.append(concatImports(tabComponent[0]))
    tab.append(concatVariables(tabComponent[1]))
    tab.append(concatHtml(tabComponent[2]))
    str = str.format(imports=tab[0], variables=tab[1], html=tab[2])
    print(str)
    return (str)