import React from 'react';
import ReactDOM from 'react-dom';
import './reset.css';
import './index.css';
import Map from './Map'

let response;

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
        var details = {
            start: this.state.start,
            end: this.state.end
        };
        
        var formBody = [];
        for (var property in details) {
          var encodedKey = encodeURIComponent(property);
          var encodedValue = encodeURIComponent(details[property]);
          formBody.push(encodedKey + "=" + encodedValue);
        }
        formBody = formBody.join("&");     

        response = fetch("http://127.0.0.1:5000/direction", {
            method: 'POST',
            headers: {
                Accept: 'application/json, text/plain, */*',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formBody
        }).then(
            res => {
                if (res.statusText === 'OK') {
                    console.log(res.json())
                } else {
                    alert("HTTP-Error: " + res.status)
                }
            }
        );
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
                <Map path={response}/>
            </div>
            

        );
    }
}
ReactDOM.render(
    <App />,
    document.getElementById('root')
)