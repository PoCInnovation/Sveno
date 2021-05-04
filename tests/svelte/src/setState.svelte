<script>
    let clicks = 0;
    function IncrementItem() {
      clicks += 1;
    }
</script>


<button on:click={IncrementItem}>Count is {clicks}</button>