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

// Runs on load of the page
$(document).ready(function () {
    // Local Javascript
    // Where you want to render the map.
    var element = document.getElementById('osm-map');

    // Height has to be set. You can do this in CSS too.
    //element.style = 'height:300px;';

    // Create Leaflet map on map element.
    var map = L.map(element);

    // Add OSM tile layer to the Leaflet map.
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Target's GPS coordinates.
    var Center_of_US = L.latLng('38.73056', '-98.22811'); // Ellsworth, Kansas
    var Grants_Pass = L.latLng('42.43875357273819', '-123.32664012908937'); // Grants Pass Oregon
    
    // Set map's center to target with zoom 14.
    map.setView(Center_of_US, 5);

    // Place a marker on the same location.
    L.marker(Center_of_US).addTo(map);
    L.marker(Grants_Pass).addTo(map);
    map.on('moveend', () => {

        console.log("_____________________________________");
        console.log("Center: " + map.getCenter());
        console.log("North:\t" + JSON.safeStringify(map.getBounds(),2))
        console.log("_____________________________________");
    });
    map.on('click', (event) => {

        console.log(" ___");
        console.log("|   |");
        console.log(event['latlng']['lat'] + ", " + event['latlng']['lng']);
        console.log("|___|");

        L.marker(event['latlng']).addTo(map);
    });
})


