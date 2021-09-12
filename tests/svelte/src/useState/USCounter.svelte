<script>
  import { afterUpdate, onDestroy } from "svelte";

  let count = 0;

  onDestroy(() => {
    "Element destroyed";
  });
  afterUpdate(() => {
    console.log(`count is now ${count}`);
  });

  const IncrementItem = () => {
    count = count + 1;
  };
</script>

<button on:click={IncrementItem}>Count is {count}</button>

<style>
</style>
