from numpy import array
import regex
from regex.regex import Pattern

REGEXP = {
   "Import Css": regex.compile(r'import\s+\'(.*.css)\''),
   "Path Css": regex.compile(r'.*\/(.*)'),
   "Class Css": regex.compile(r'class=\"(.*)\"')
}

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
      return (css)
   else :
      return (css)