/*
 * This script contains all functions needed to parse an array of User objects,
 * a JS  object literal with
 * {username: string, realname: string, location: {lat: number, lng: number}}
 */

function showWorld(map) {
  /* Changes map to show world view
   */
  map.setCenter(new google.maps.LatLng(0, 0));
  map.setZoom(2);
}

function geolocateUser(map) {
  /* Centres map to user's geolocation and sets a marker, if the user
   * rejects user location request, then zooms out to world view
   */
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                   position.coords.longitude);
      map.setCenter(pos);

      // add a marker representing the player location
      var userMarker = new google.maps.Marker({
        title:'You',
        map: map,
        position: pos,
        animation: google.maps.Animation.DROP,
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
      });

    }, function() {
      // user said no
      showWorld(map);
    });
  } else {
    // browser does not support geolocation in this case show world view of map
    showWorld(map);
  }
}

function addMarker(map, user) {
  /* adds a marker for every user with  info window
   * to map.
   */
  setTimeout(function() {
    // add marker for user
    var marker = new google.maps.Marker({
      title: user.realname,
      map: map,
      position: user.position,
      animation: google.maps.Animation.DROP
    });
    // add info window
    var infowindow = new google.maps.InfoWindow({
      content: user.realname
    });

    // add click listener
    google.maps.event.addListener(marker, 'click', function() {
      if (currentInfoWindow) {currentInfoWindow.close()};
      if (currentInfoWindow !== infowindow) {
        currentInfoWindow = infowindow;
        infowindow.open(map, marker);
      } else {
        currentInfoWindow = null;
      }
    });
  }, 20);
}

function initialize(userArray) {
  /* Initializes google Map object in DOM with ID 'map-canvas'
   * centred at the users location. For the map to show locally, the
   * user must accept the prompt asking for location services. Otherwise
   * we show a global view.
   *
   * The function iterates over the array of user objects and adds a marker
   * for each on the map
   */
  var mapOptions = {zoom: 13};
  // make the map
  var map = new google.maps.Map(document.getElementById('map-canvas'),
                                mapOptions);

  // use HTML5 geolocation to set the center of the map as user's location
  geolocateUser(map);

  // now iterate over userArray and add each to map as marker
  userArray.forEach(function(user) {addMarker(map, user);});

}

var currentInfoWindow = null;

// ---- generate some random users to test ----
var names = ['bill gates', 'steve jobs', 'mark zuckerberg', 'drew houston',
            'satya nadella', 'bob jones'];

var users = [];
for (var i = 0; i < 100; i++) {
  var name = names[Math.floor(Math.random() * names.length)];
  var usrObj = {
    realname: name,
    position: {lat: (2 * Math.random() - 1) * 90, lng: (2 * Math.random() - 1) * 180},
    username: 'haxx0r'
  }
  users.push(usrObj);
}

google.maps.event.addDomListener(window, 'load', function() {initialize(users);});
