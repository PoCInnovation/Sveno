import React from 'react'
import './App.css'

class Welcome extends React.Component {
  render() {
    return <h1 className="App">Bonjour, {this.props.name}</h1>;
  }
}

class Test extends React.Component {
  render() {
    return <h1>Test</h1>;
  }
}

export default Welcome;