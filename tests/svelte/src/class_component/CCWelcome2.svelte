<script>
    import axios from 'axios'
	import { onMount, onDestroy } from 'svelte'

    export let name = undefined

    onMount(() => {
    console.log(`Hello, ${this.props.name}`)
  })
	onDestroy(() => {
    console.log(`Goodbye, ${this.props.name}`)
  })

    

</script>

 <h1>Test: salut {name}</h1>

<style>
</style>
