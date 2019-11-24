import React, { Component, PropTypes } from "react";
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  Polyline
} from "react-google-maps";

class Testme extends React.Component {
    constructor(props) {
        super(props);
        console.log('im in child fo real');
        console.log(props);
        this.state = { routes: [], finishedRoutes: [] };
      }

  drawPath() {
    let i = 0;

    if (this.props.render) {
        console.log("im fucking retarded")
        console.log(this.props.routesB);
      return (
        <React.Fragment>
          {this.props.routesB.map(step => (
            <Polyline
              key={i++}
              path={[
                { lat: step.lat1.lat, lng: step.lat1.lng },
                { lat: step.lng1.lat, lng: step.lng1.lng }
              ]}
              options={step.DgScr < 1 ? {strokeColor: "#00FF00"} : step.DgScr < 2 ? {strokeColor: "#FFFF00"} : {strokeColor: "#FF0000"}}
            />
          ))}
        </React.Fragment>
      );
    }
  }
  renderMap() {
    let temp = this.drawPath();
    this.setState({ finishedRoutes: temp });
  }

  componentDidMount(){
      this.renderMap();
  }

  render() {
    console.log(this.props);
    return <div>We made it</div>;
  }
  render() {
    const {routesB, render} = this.props;
    return (
      <GoogleMap
        defaultZoom={12}
        defaultCenter={{ lat: 43.011173, lng: -81.273547 }}
      >
        {this.state ? this.state.finishedRoutes : 'bruh'}
      </GoogleMap>
    );
  };
}

let TestmeReal = withScriptjs(withGoogleMap(Testme));

class TestmeReal2 extends React.Component {
    render() {
        return (<TestmeReal
            routesB={this.props.routesB}
            render={this.props.render}
            googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyA05IZP-_GDgylMrM22XBYZ9qUxiTXjq-w&v=3.exp&libraries=geometry,drawing,places"
            loadingElement={<div style={{ height: `100%` }} />}
            containerElement={<div style={{ height: `auto`, width: "100vw" }} />}
            mapElement={<div style={{ height: `100%` }} />}
          />);
    }
};

export default TestmeReal2;