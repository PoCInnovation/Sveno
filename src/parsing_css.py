
import regex

REGEXP = {
   "Import Css": regex.compile(r'import\s+\'(.*.css)\''),
   "Path Css": regex.compile(r'.*\/(.*)'),
   "Tag Css": regex.compile(r'.(App)\s+(\{(?:[^.@]+|(?2))\})'),
   "Class Css": regex.compile(r'class=(\"((?:[^\"]+|(?1)))\")'),
   "@ Css": regex.compile(r'@.*\{(?:[^.]+|(?0))\}')
}

TEMPLATE_TAG_CSS = r'.{var}{end}'

def search_spe_class(css, final_css):
   spe_css = REGEXP['@ Css'].findall(css)

   if final_css:
      final_css = final_css + '\n' + spe_css[0]
   return (final_css)

def search_class(content, css):
   class_names = REGEXP['Class Css'].findall(content)
   end = r'\s+\{(?:[^.@]+|(?0))\}'
   final_css = ''

   if class_names:
      for name in class_names:
         pattern = TEMPLATE_TAG_CSS.format(var=name[1], end=end)
         re_pattern = regex.compile(pattern)
         pattern = re_pattern.findall(css)
         final_css = final_css + '\n' + pattern[0]
   final_css = search_spe_class(css, final_css)
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


