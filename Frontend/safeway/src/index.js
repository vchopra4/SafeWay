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
    render() {
        return (
            <div className="search">
                <input className="start" placeholder="Start"></input>
                
                <input className="end" placeholder="End"></input>

                <input className="submit" type="submit"></input>
            </div>
            
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