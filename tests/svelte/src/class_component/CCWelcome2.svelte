{
  render() {
    return <h1>Test: salut {this.props.name}</h1>;
  }
  componentDidMount(props) {
    console.log(`Hello, ${this.props.name}`)
  }
  componentWillUnmount(props) {
    console.log(`Goodbye, ${this.props.name}`)
  }
}