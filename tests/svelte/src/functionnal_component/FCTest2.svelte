<script>
    import { onMount } from 'svelte'
	import { onMount, onDestroy } from 'svelte'
	import { afterUpdate, onDestroy } from 'svelte'

    

    onDestroy(() => {
            console.log("and this on destroy");
        })
	afterUpdate(() => {
        console.log("print this after update");
        
    })

    function test() {

    let i = 0;

}

</script>


        <div>ok</div>
    

<style>
</style>
