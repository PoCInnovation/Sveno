import React from 'react'
import './App.css'

class SSCounter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          count: 0
        };
      }

    IncrementItem = () => {
        this.setState({count: this.state.count + 1})
    }

    notExportedVar = 5;

    render() {
        return (
        <div>
          <button onClick={this.IncrementItem}>Count is {this.props.count}</button>
          <p>this var should be undefined but exported {this.props.undefinedVar}</p>
        </div>);
    }
}

export default Counterr;