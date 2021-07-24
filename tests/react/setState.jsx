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
        this.setState({clicks: this.state.count + 1})
    }

    render() {
        return <button onClick={this.IncrementItem}>Count is {this.props.count}</button>;
    }
}

export default Counterr;