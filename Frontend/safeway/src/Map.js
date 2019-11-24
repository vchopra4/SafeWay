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

  render() {
    console.log(this.props);
    return (
      <GoogleMap
        defaultZoom={12}
        defaultCenter={{ lat: 43.011173, lng: -81.273547 }}
      >
        {this.drawPath()}
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
