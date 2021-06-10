import React from 'react'
import './App.css'

class SSCounter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          clicks: 0
        };
      }

    IncrementItem = () => {
        this.setState({clicks: this.state.clicks + 1})
    }

    render() {
        return <button onClick={this.IncrementItem}>{this.props.number}</button>;
    }
}

export default Counterr;