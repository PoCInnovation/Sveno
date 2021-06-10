TEMPLATE_SVELTE = """<script>
    {imports}

    {variables}

    {functions}

</script>

{html}
"""

TEMPLATE_VARIABLE = "{qualifier} {name} = {value}"

TEMPLATE_FUNCTION = "{qualifier} {name} = {args} => {content}"