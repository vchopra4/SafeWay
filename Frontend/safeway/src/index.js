import React from 'react';
import ReactDOM from 'react-dom';
import './reset.css';
import {
    withGoogleMap,
    withScriptjs,
    GoogleMap,
    Polyline
  } from "react-google-maps";
import './index.css';
import Map from './Map'
import Testme from './TestMe';

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

        fetch("http://127.0.0.1:5000/direction", {
            method: 'POST',
            headers: {
                Accept: 'application/json, text/plain, */*',
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formBody
        }).then(function(u){
            return u.json();
        })
        .then(
            res => {
                this.props.onEnterLocation(res);
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
    constructor(props) {
        super(props);
        this.state = {paths: [1,2,3,4], render: false, finishedPaths: []};
    }

    handleChange = (roads) => {
        this.setState({paths: roads, render: true});
    }

    drawPath() {
        let i = 0;
    
        if (this.state.render) {
          return (
            <React.Fragment>
              {this.state.paths.map(step => (
                <Polyline
                  key={i++}
                  path={[
                    { lat: step.lat1, lng: step.lng1 },
                    { lat: step.lat2, lng: step.lng2 }
                  ]}
                  options={{ strokeColor: "#FF0000" }}
                />
              ))}
            </React.Fragment>
          );
        }
      };

    render() {

        console.log(
            'im in parent'
        );
        let myComp ;
        if (this.state.render && this.state.paths) {
            myComp = <Testme routesB={this.state.paths} render={this.state.render} />;
        } else {
            myComp = <div/>;
        }
        
        return (
            <div className="app">
                <Topbar />
                <Search onEnterLocation={this.handleChange} />
                {myComp}
            </div>
            

        );
    }
}
ReactDOM.render(
    <App />,
    document.getElementById('root')
)