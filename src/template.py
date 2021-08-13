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

TEMPLATE_LIFECYCLE = "{kind}(() => {content})"

TEMPLATE_SVELTE_IMPORTS = "{{ {imports} }}"

TEMPLATE_IMPORTS = "import {imports} from '{origin}'"

TEMPLATE_REACT_DOM_RENDER = """const {name} = new {component}({{
    target: {target}
}})
"""