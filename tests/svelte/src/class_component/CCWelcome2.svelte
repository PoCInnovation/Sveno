<script>
  import axios from "axios";
  import FCTest2 from "../functionnal_component/FCTest2";
  import { onMount, onDestroy } from "svelte";

  export let name = undefined;

  onMount(() => {
    console.log(`Hello, ${this.props.name}`);
  });
  onDestroy(() => {
    console.log(`Goodbye, ${this.props.name}`);
  });

  const componentDidMount = (props) => {
    console.log(`Hello, ${this.props.name}`);
  };
  const componentWillUnmount = (props) => {
    console.log(`Goodbye, ${this.props.name}`);
  };
</script>

<h1>Test: salut {name}</h1>

<style>
</style>
