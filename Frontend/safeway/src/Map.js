import React from "react";
import PropTypes from 'prop-types'
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  Polyline
} from "react-google-maps";

class Map extends React.Component {
  constructor(props) {
    super(props);
    console.log('im in child');
    console.log(props);
    this.state = { routes: [], finishedRoutes: [] };
  }

  drawPath() {
    let i = 0;

    if (this.props.render) {
      return (
        <React.Fragment>
          {this.props.routesB.map(step => (
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
  componentDidMount(){
    console.log('here');
    console.log(this.state);
    console.log(this.props);
    this.renderMap();
  }

  componentWillReceiveProps(props) {
    console.log('will i recieve shit?');
    console.log(this.props);
    console.log(props);
    
  }

  renderMap(){
    let temp = this.drawPath();
    this.setState({finishedRoutes: temp});
  }

  render() {
    console.log(this.state);
    console.log(this.props);
    const {routesB, render} = this.props;
    console.log(routesB)
    console.log(render);
    return (
      <GoogleMap
        defaultZoom={12}
        defaultCenter={{ lat: 43.011173, lng: -81.273547 }}
      >
        {this.state.finishedRoutes}
      </GoogleMap>
    );
  };
}

let MapComponent = withScriptjs(withGoogleMap(Map));

export default () => (
  <MapComponent
    googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyA05IZP-_GDgylMrM22XBYZ9qUxiTXjq-w&v=3.exp&libraries=geometry,drawing,places"
    loadingElement={<div style={{ height: `100%` }} />}
    containerElement={<div style={{ height: `auto`, width: "100vw" }} />}
    mapElement={<div style={{ height: `100%` }} />}
  />
);