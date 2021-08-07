<script>
    import { onMount } from 'svelte'
	import { onMount, onDestroy } from 'svelte'
	import { afterUpdate, onDestroy } from 'svelte'

    export let name = undefined

    onMount(() => {
        console.log("Print this on mount");
    })

    function test() {

    let i = 0;

}

</script>

 <h1>Salut, {name}</h1>

<style>
</style>
