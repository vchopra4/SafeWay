import React from 'react';
import ReactDOM from 'react-dom';
import './reset.css';
import './index.css';
import Map from './Map'

class Topbar extends React.Component {
    render() {
        return (
            <div className="topbar">
                <h1>SAFEWAY</h1>
            </div>
            
        )
    }
}

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {start: '', end: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }
    handleChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }
    handleSubmit(event) {
        // this line represents the information for the post request
        alert('Start: ' + this.state.start + ", End: " + this.state.end);
        event.preventDefault();
    }
    render() {
        return (
            <form className="search" onSubmit={this.handleSubmit}>
                <input className="start" name="start" placeholder="Start" value={this.state.start} onChange={this.handleChange}></input>
                
                <input className="end" name="end" placeholder="End" value={this.state.end} onChange={this.handleChange}></input>

                <input className="submit" type="submit" value="Submit"></input>
            </form>
            
        )
    }
}
class App extends React.Component {
    render() {
        return (
            <div className="app">
                <Topbar />
                <Search />
                <Map />
            </div>
            

        );
    }
}
ReactDOM.render(
    <App />,
    document.getElementById('root')
)