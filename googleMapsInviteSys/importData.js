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

function initialize() {
  /* Initializes google Map object in DOM with ID 'map-canvas'
   * centred at the users location. For the map to correctly show, the
   * user must accept the prompt asking for location services.
   */
  var mapOptions = {zoom: 13};
  // make the map
  var map = new google.maps.Map(document.getElementById('map-canvas'),
                                mapOptions);

  // use HTML5 geolocation to set the center of the map as user's location
  geolocateUser(map);
}

google.maps.event.addDomListener(window, 'load', initialize);






//   //###################
//   var myLatlng = {lat: -30.397, lng: 150.644};
//   var mapOptions = {
//     zoom: 8,
//     center: myLatlng
//   };

//   // make the map
//   var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

//   // make the info window for marker on click
//   var contentString = '<div id="content">'+
//       '<div id="siteNotice">'+
//       '</div>'+
//       '<h1 id="firstHeading" class="firstHeading">Uluru</h1>'+
//       '<div id="bodyContent">'+
//       '<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
//       'sandstone rock formation in the southern part of the '+
//       'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) '+
//       'south west of the nearest large town, Alice Springs; 450&#160;km '+
//       '(280&#160;mi) by road. Kata Tjuta and Uluru are the two major '+
//       'features of the Uluru - Kata Tjuta National Park. Uluru is '+
//       'sacred to the Pitjantjatjara and Yankunytjatjara, the '+
//       'Aboriginal people of the area. It has many springs, waterholes, '+
//       'rock caves and ancient paintings. Uluru is listed as a World '+
//       'Heritage Site.</p>'+
//       '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">'+
//       'https://en.wikipedia.org/w/index.php?title=Uluru</a> '+
//       '(last visited June 22, 2009).</p>'+
//       '</div>'+
//       '</div>';

//   var infowindow = new google.maps.InfoWindow({
//       content: contentString
//   });

//   // finally add the marker
//   var marker = new google.maps.Marker({
//       position: myLatlng,
//       map: map,
//       title: 'hello'
//   });
//   // add click listener
//   google.maps.event.addListener(marker, 'click', function() {
//     infowindow.open(map,marker);
//   });

// google.maps.event.addDomListener(window, 'load', initialize);


// google.maps.Infowindow({content: "abd", maxWidth: 100});

// use to drop an array of markers in sequence

// function drop() {
//   for (var i =0; i < markerArray.length; i++) {
//     setTimeout(function() {
//       addMarkerMethod();
//     }, i * 200);
//   }
// }
