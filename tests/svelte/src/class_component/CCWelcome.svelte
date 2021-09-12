<script>
  import axios from "axios";
  import FCTest2 from "../functionnal_component/FCTest2";

  export let name = undefined;

  const componentDidMount = (props) => {
    console.log(`Hello, ${this.props.name}`);
  };
  const componentWillUnmount = (props) => {
    console.log(`Goodbye, ${this.props.name}`);
  };
</script>

<h1 class="App">Bonjour, {name}</h1>

<style>
</style>
