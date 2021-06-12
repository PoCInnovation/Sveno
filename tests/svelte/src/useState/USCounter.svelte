<script>
  let count = 0;

  const IncrementItem = () => {
    count = count + 1;
  };

</script>

<button on:click={IncrementItem}>Count is {count}</button>

<style>
</style>
