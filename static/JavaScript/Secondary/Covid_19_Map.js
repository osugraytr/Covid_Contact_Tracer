// //  //   //  // //// //  //   //  // //// //  //   //  // //// //  //   //  // //// //  //   //  // //
// String Manipulation

// safely handles circular references
JSON.safeStringify = (obj, indent = 2) => {
    let cache = [];
    const retVal = JSON.stringify(
        obj,
        (key, value) =>
            typeof value === "object" && value !== null
                ? cache.includes(value)
                    ? undefined // Duplicate reference found, discard key
                    : cache.push(value) && value // Store value in our collection
                : value,
        indent
    );
    cache = null;
    return retVal;
};
// //  //   //  // //// //  //   //  // //// //  //   //  // //// //  //   //  // //// //  //   //  // //

// ||  ||   ||  || |||| ||  ||   ||  || |||| ||  ||   ||  || |||| ||  ||   ||  || |||| ||  ||   ||  || ||
// Back End Calls using AJAX


// ||  ||   ||  || |||| ||  ||   ||  || |||| ||  ||   ||  || |||| ||  ||   ||  || |||| ||  ||   ||  || ||

// ##  ##   ##  ## #### ##  ##   ##  ## #### ##  ##   ##  ## #### ##  ##   ##  ## #### ##  ##   ##  ## ##
// Functions to do mechanical things on the front end

// ##  ##   ##  ## #### ##  ##   ##  ## #### ##  ##   ##  ## #### ##  ##   ##  ## #### ##  ##   ##  ## ##

// Removes all markers from the map
function Remove_All_Marker_Points(Marker_Layers) {
    for (i = 0; i < Marker_Layers.length; i++) {
        Marker_Layers[i].remove();
        console.log("Remove:\t" + JSON.safeStringify(Marker_Layers[i]['_latlng']))
    }
}

// Unpacks teh Box range to make it easier to read
function Seperate_Box_Range( Box_Range ) {

    _Box_Range = {}

    _Box_Range['West'] = Box_Range['_southWest']['lat']
    _Box_Range['South'] = Box_Range['_southWest']['lng']
    _Box_Range['East'] = Box_Range['_northEast']['lat']
    _Box_Range['North'] = Box_Range['_northEast']['lng']

    return _Box_Range
}

// Returns True if the marker is within the box, Returns False if not
function Within_Box_Bool( LatLng, Box_Range ) {

    Clean_Box_Range = Seperate_Box_Range(Box_Range);

    //console.log( Clean_Box_Range[ 'West' ] )
    //console.log( Clean_Box_Range[ 'South' ] )
    //console.log( Clean_Box_Range[ 'East' ] )
    //console.log( Clean_Box_Range[ 'North' ] )

    Lat = LatLng[ 'lat' ]
    Lng = LatLng[ 'lng' ]
    
    if ( Clean_Box_Range[ 'West' ] <= Lat && Lat <= Clean_Box_Range[ 'East' ] ) {
        if ( Clean_Box_Range[ 'South' ] <= Lng && Lng <= Clean_Box_Range[ 'North' ] ) {
            //console.log( "Inside Box:\t", Lat, " + ", Lng );
            return true;
        }
    }

    return false;
}

//Remove All Marker Points Within bounds
function Remove_Marker_Points_Within_Box( Marker_Layers, Box_Range ) {
    for ( i = 0; i < Marker_Layers.length; i++ ) {
        
        // Returns True if the marker is within the box, Returns False if not
        if ( Within_Box_Bool( Marker_Layers[i]['_latlng'], Box_Range ) ) {

            // Remove marker at position i
            
            //console.log("Remove:\t" + JSON.safeStringify(Marker_Layers[i]['_latlng']))
        }
        else {
            // Should get in here if the marker is not in the current view
            Marker_Layers[i].remove();
        }
    }
}

// Set map's center to target with zoom 14.
function Set_Map_View( Placement, Zoom, map ) {
    map.setView( Placement, Zoom );
}

// Place a marker on the same location.
function Place_Map_Marker( Placement, map ) {
    Marker_Layers.push(L.circleMarker( Placement ).addTo(map));
}

// Get Zoom level
function Get_Zoom_Level( map ) {
    return map.getZoom();
}

// Sets [ Lat, Lng] to the correct format
function Set_LatLng( Lat, Lng ) {
    return L.latLng( Lat, Lng );
}

// 
function Place_Map_Markers(Marker_Array, Box_Range, map ) {
    for (i = 0; i < Marker_Array.length; i++ ) { 
        // Returns True if the marker is within the box, Returns False if not
        if ( Within_Box_Bool( Marker_Array[i], Box_Range ) ) {

            // Remove marker at position i
            
            //console.log("Remove:\t" + JSON.safeStringify(Marker_Layers[i]['_latlng']))
            Place_Map_Marker(Set_LatLng(Marker_Array[i]['lat'], Marker_Array[i]['lng']), map);

        }
        else {
            // Don't add the marker
        }
    }
}

function Merge_New_And_Current( New_Markers ) {
    for (i = 0; i < New_Markers.length; i++) {
        var New_Marker = Set_LatLng(Marker_Array[i]['lat'], Marker_Array[i]['lng'])

        if ( Marker_Layers.includes( New_Marker ) ) {
            // Do not add
        }
        else {
            Place_Map_Marker( New_Marker, map );
        }
    }
}

// Sets Markers after calling the backend
function Set_Covid_Tracking_Points( map ) {

    var Box_Range = map.getBounds(  );

    // Do an ajax call to get results markers inside bounds
    New_Markers = [{ 'lat': '42.43875357273819', 'lng': '-123.32664012908937' },{ 'lat': '42.42875357273819', 'lng': '-123.31664012908937' }, { 'lat': '42.44875357273819', 'lng': '-123.33664012908937' } ];

    //Marker_Layers = Merge_New_And_Current( New_Markers );

    //console.log( Get_Zoom_Level( map ) );
    Place_Map_Markers( New_Markers, Box_Range, map );
}

// Default Map View
function Default_Map_Layout( map ) {

    // Add OSM tile layer to the Leaflet map.
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    Set_Map_View( Center_of_US, 5, map );
    //Place_Map_Marker( Center_of_US, map );
}

// --  --   --  -- ---- --  --   --  -- ---- --  --   --  -- ---- --  --   --  -- ---- --  --   --  -- --
// Start up script and event handlers and globals

// Layer used for adding and removing markers
var Marker_Layers = [] // Marker_Layers.push(L.circleMarker( Placement ).addTo(map));
var Coordinate_Locations = [  ] // { 'lat': '42.43875357273819', 'lng': '-123.32664012908937' }

// Target's GPS coordinates.
var Center_of_US = L.latLng( '38.73056', '-98.22811' ); // Ellsworth, Kansas
var Grants_Pass = L.latLng( '42.43875357273819', '-123.32664012908937' ); // Grants Pass Oregon

// Min_Zoom
var Min_Zoom = 14;

// Runs on load of the page
$(document).ready(function () {
    // Local Javascript

    // Where you want to render the map.
    var element = document.getElementById('osm-map');

    // Create Leaflet map on map element.
    var map = L.map(element);

    // Set default map view
    Default_Map_Layout( map );

    // Get Covid markers
    //Set_Covid_Tracking_Points( map );

    map.on('moveend', () => {

        //console.log("_____________________________________");
        //console.log("Center: " + map.getCenter());
        //console.log("North:\t" + JSON.safeStringify(map.getBounds(), 2));
        //console.log("_____________________________________");

        var Box_Range = map.getBounds();

        //Remove All Marker Points Within bounds
        if ( Get_Zoom_Level( map ) < Min_Zoom ) {
            // If Zoom is less than 13 remove all Map_Markers
            Remove_All_Marker_Points(Marker_Layers);
        }
        else {
            // If Zoom is larger than 12 remove all Map_Markers outside of the box view
            Remove_Marker_Points_Within_Box( Marker_Layers, Box_Range );
            Set_Covid_Tracking_Points( map );
        }
    });

    map.on('click', (event) => {

        console.log(" ___");
        console.log("|   |");
        console.log(event['latlng']['lat'] + ", " + event['latlng']['lng']);
        console.log("|___|");

        

        //Remove All Marker Points Within bounds
        if ( Get_Zoom_Level(map) < Min_Zoom ) {
        }
        else {
            // If Zoom is larger than 12 Add a marker
            Place_Map_Marker( event['latlng'], map );
        }
    });
})
// --  --   --  -- ---- --  --   --  -- ---- --  --   --  -- ---- --  --   --  -- ---- --  --   --  -- --