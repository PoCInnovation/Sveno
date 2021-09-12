<script>
  export let count = 0;
  export let undefinedVar = undefined;

  const IncrementItem = () => {
    this.setState({ count: this.state.count + 1 });
  };
</script>

<div>
  <button on:click={IncrementItem}>Count is {count}</button>
  <p>this var should be undefined but exported {undefinedVar}</p>
</div>

<style>
</style>
