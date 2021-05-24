from typing import final
from numpy import array, e
import regex
from regex.regex import Pattern

REGEXP = {
   "Import Css": regex.compile(r'import\s+\'(.*.css)\''),
   "Path Css": regex.compile(r'.*\/(.*)'),
   "Tag Css": regex.compile(r'.(App)\s+(\{(?:[^.@]+|(?2))\})'),
   "Class Css": regex.compile(r'class=(\"((?:[^\"]+|(?1)))\")')
}

TEMPLATE_TAG_CSS = '.{var}'
TEMPLATE_SPE_FLAG = '|@.*({var}).*(\{(?:[^.]+|(?1))\})'

def search_class(content, css):
   # print("content = ", content)
   class_names = REGEXP['Class Css'].findall(content)
   end = '\s+\{(?:[^.@]+|(?0))\}'
   final_css = ''

   if class_names:
      for test in class_names:
         begin = TEMPLATE_TAG_CSS.format(var=test[1])
         pattern = begin + end
         re_pattern = regex.compile(pattern)
         pattern = re_pattern.findall(css)
         final_css = final_css + '\n' + pattern[0]
   print(final_css)
   return (final_css)

def openCssFile(result, path):
   Pattern = REGEXP['Path Css'].findall(path)
   result = regex.sub('./', '', result)
   path = regex.sub(Pattern[0], result, path)
   fd = open(path, 'r')
   return (fd.read())

def parseCss(content, path):
   result = REGEXP['Import Css'].findall(content)
   css = ''

   if result:
      css = openCssFile(result[0], path)
      css = search_class(content, css)
      return (css)
   else :
      return (css)


