import React from 'react'
import axios from 'axios'
import FCTest2 from './functionnal_component';

class CCWelcome extends React.Component {
  render() {
    return <h1 className="App">Bonjour, {this.props.name}</h1>;
  }
}

class CCWelcome2 extends React.Component {
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

export default Welcome;