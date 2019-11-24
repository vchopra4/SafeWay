import React from "react";
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  Polyline
} from "react-google-maps";

class Map extends React.Component {
  constructor(props) {
    super(props);
    this.state = {paths: [], isRendered: false};
  }
  path = [
    { lat: 18.558908, lng: -68.389916 },
    { lat: 18.558853, lng: -68.389922 },
    { lat: 18.558375, lng: -68.389729 },
    { lat: 18.558032, lng: -68.389182 },
    { lat: 18.55805, lng: -68.388613 },
    { lat: 18.558256, lng: -68.388213 },
    { lat: 18.558744, lng: -68.387929 }
  ];

path2=[{ lat1: 18.558908, lng1: -68.389916, lat2: 18.558853, lng2: -68.389922}]

  drawPath = () => {
    let pathLine = [];

    let i = 0;

    console.log(this.props.path);
    console.log(this.props.renderP);
    
    return (
      <React.Fragment>
        {this.path2.map(step => (
          <Polyline
            key={i++}
            path={[{lat: step.lat1, lng: step.lng1}, {lat: step.lat2, lng: step.lng2}]}
            options={{ strokeColor: "#FF0000" }}
          />
        ))}
      </React.Fragment>
    );

    return pathLine;
  };

  render = () => {
    return (
      <GoogleMap
        defaultZoom={16}
        defaultCenter={{ lat: 18.559008, lng: -68.388881 }}
      >
        {this.drawPath()}
        {/* <Polyline path={this.path} options={{ strokeColor: "#FF0000 " }} /> */}
      </GoogleMap>
    );
  };
}

const MapComponent = withScriptjs(withGoogleMap(Map));

export default () => (
  <MapComponent
    googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyA05IZP-_GDgylMrM22XBYZ9qUxiTXjq-w&v=3.exp&libraries=geometry,drawing,places"
    loadingElement={<div style={{ height: `100%` }} />}
    containerElement={<div style={{ height: `auto`, width: "100vw" }} />}
    mapElement={<div style={{ height: `100%` }} />}
  />
);
