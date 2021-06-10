<script>
  const IncrementItem = () => {
    setCount(count + 1);
  };

</script>

<button on:click={IncrementItem}>Count is {count}</button>
