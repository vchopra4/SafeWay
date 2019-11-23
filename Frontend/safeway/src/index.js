import React from 'react';
import ReactDOM from 'react-dom';
import './reset.css';
import './index.css';

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
class Map extends React.Component {
    render() {
        return (
            <div class="map">
                <iframe width="100%" height="450" frameborder="0" style={{border:0}}
src="https://www.google.com/maps/embed/v1/place?q=place_id:ChIJ0SvEag7uLogRm3m5qlPzh6o&key=..." allowfullscreen></iframe>
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