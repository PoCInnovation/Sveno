# import regex

# REGEXP_TEST = {
#     "function": regex.compile(r'(function.*\))', regex.MULTILINE),
#     "Imports": regex.compile(r"import.*"),
#     "HTML": regex.compile(r'(<(?:[^)(]+|(?1))*+)', regex.MULTILINE),
#     "Variable": regex.compile(r'(const|let|var)\s+([a-zA-Z0-9_-]+)\s*=\s*([^;]+)', regex.MULTILINE),
#     "ClassName": regex.compile(r"className")
# }

# def getHtmlComponents(content):
#     content = regex.sub("className", "class", content)
#     htmlComponents = REGEXP_TEST["HTML"].findall(content)
#     return (htmlComponents)

# def getImportsComponents(content):
#     importsComponents = REGEXP_TEST["Imports"].findall(content)
#     return (importsComponents)

# def getFunctionComponents(content):
#     functionComponents = REGEXP_TEST["function"].findall(content)
#     return (functionComponents)

# def getVariableComponents(content):
#     varComponents = REGEXP_TEST["Variable"].findall(content)
#     return (varComponents)