<script>
  export let number = undefined;

  const IncrementItem = () => {
    this.setState({ clicks: this.state.clicks + 1 });
  };

</script>

<button on:click={IncrementItem}>{number}</button>

<style>
</style>
