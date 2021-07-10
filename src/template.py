TEMPLATE_SVELTE = """<script>
    {imports}

    {variables}

    {lifeCycle}

    {functions}

</script>

{html}

<style>{style}
</style>
"""

TEMPLATE_VARIABLE = "{qualifier} {name} = {value}"

TEMPLATE_FUNCTION = "{qualifier} {name} = {args} => {content}"

TEMPLATE_LIFECYCLE = "{kind}({args} => {content})"
