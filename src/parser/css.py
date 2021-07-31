import regex

REGEXP = {
   "Import Css": regex.compile(r'import\s+\'(.*.css)\''),
   "Path Css": regex.compile(r'.*\/(.*)'),
   "Tag Css": regex.compile(r'.(App)\s+(\{(?:[^.@]+|(?2))\})'),
   "Class Css": regex.compile(r'class=(\"((?:[^\"]+|(?1)))\")'),
   "@ Css": regex.compile(r'@.*\{(?:[^.]+|(?0))\}'),
   "in @media Css": regex.compile(r'@media.*(\{(?:[^}{]+|(?1))*+\})'),
   "out @media Css": regex.compile(r'@media[^{]*')
}

TEMPLATE_TAG_CSS = r'.{var}{end}'

def search_spe_class(css, final_css):
   spe_css = REGEXP['@ Css'].findall(css)
   in_media_css = REGEXP['in @media Css'].findall(css)
   out_media_css = REGEXP['out @media Css'].findall(css)

   if final_css:
      if len(spe_css):
         final_css = final_css + '\n' + spe_css[0]
      if len(out_media_css):
         final_css = final_css + '\n' + (out_media_css[0])
      if len(in_media_css):
         final_css = final_css + in_media_css[0]
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
         if len(pattern):
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
   else:
      return (css)


