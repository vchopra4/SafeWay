import React from 'react';
import ReactDOM from 'react-dom';
import './reset.css';
import './index.css';
import Map from './Map'

class Topbar extends React.Component {
    render() {
        return (
            <div className="topbar">
                <h1>Safeway</h1>
            </div>
            
        )
    }
}

class Search extends React.Component {
    render() {
        return (
            <div className="search">
                <input className="start" placeholder="start"></input>
                
                <input className="end" placeholder="end"></input>
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