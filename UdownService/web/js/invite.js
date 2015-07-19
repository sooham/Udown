/*
 * This script contains all functions needed to parse an array of User objects,
 * which is a JS object literal with
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
        animation: google.maps.Animation.DROP
      });

    }, function() {
      // user said no
      showWorld(map);
    });
  } else {
    // browser does not support geolocation in this case show world view of map
    alert('This browser does not support geolocation. ' +
          'To provide you better study partners we suggest you update' +
          'your browser');
    showWorld(map);
  }
}

function addMarker(map, user) {
  /* adds a marker for every user with  info window
   * to map.
   */
  setTimeout(function() {
    // add marker for user
    if (user.position == {lat: 0, lng: 0}) {
      return;
    }
    var marker = new google.maps.Marker({
      title: user.realname,
      map: map,
      position: user.position,
      animation: google.maps.Animation.DROP,
      icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
    });
    // add info window
    var userContent = '<div class="infowindow">' +
                        '<center><h4>' + user.realname +
                        ' (' + user.username + ')' + '</h4>' +
                        '<br><a href="#"">Invite</a></center>' +
                      '</div>';
    var infowindow = new google.maps.InfoWindow({
      content: userContent,
      minWidth: 200
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
  }, 500);
}

function getUsersFromServer(userArray) {
  /* Gets the information for every user from the server and adds their user
   * objects to the array userArray
   */
  $.ajax({
    url: 'localhost:8000/api/v1/user/',
    data: function(data) {
      // parse the data and add it to the userArray
      userArray = JSON.parse(data).objects;
    },
    dataType: 'json'
  });

  // for all user objects we need to update a bit
  userArray.forEach(function(userObj) {
    usrObj.position = {lat: usrObj.latitude, lng: usrObj.lng};
    usrObj.realname = usrObj.first_name + usrObj.last_name;
  });
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
var users = [];
// To use, add UserObjects to the users array above this line,
// then everything else will work itself

getUsersFromServer(users);
google.maps.event.addDomListener(window, 'load', function() {initialize(users);});
