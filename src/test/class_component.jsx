import React from 'react'
import test from 'test'

class Welcome extends React.Component {
  render() {
    return <h1>Bonjour, {this.props.name}</h1>;
  }
}

class Test extends React.Component {
  render() {
    return <h1>Test</h1>;
  }
}

export default Welcome;