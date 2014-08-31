  // Student Name: Sarvesh Sadhoo (1000980763)
  // Project 3: Web Mashup: Display Best Restaurants on a Map
  // Link: http://omega.uta.edu/~sxs0763/project3/yelp.html
  // Final

  var json; 
  var geocoder;
  var map;
  var markers = [];
  var input;
  var bounds;
  var southwest_latitude;
  var southwest_longitude;
  var northeast_latitude;
  var northeast_longitude;
  var gbb;

// initialize functions loads the map on the webpage!
  function initialize(){
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(32.75, -97.13);
    var mapOptions = {
      zoom: 16,
      center: latlng
    }
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    google.maps.event.addListener(map, 'bounds_changed', function() {
    bounds = map.getBounds();
    southwest_latitude = bounds.getSouthWest().lat();
    southwest_longitude = bounds.getSouthWest().lng();
    northeast_latitude = bounds.getNorthEast().lat();
    northeast_longitude = bounds.getNorthEast().lng();
    
   });
  }
// sendRequest function sends query to the Yelp api and reverts back witha JSON object!
   function sendRequest () {
    input = document.getElementById("search").value; // Checks if the input is kept blank!
    if (input == ""){
      alert("Search Cannot Be Empty. Please Enter a Value!");
      return;
    }
    var xhr = new XMLHttpRequest();
    gbb = southwest_latitude  + "," + southwest_longitude + "|" + northeast_latitude  + "," + northeast_longitude;
    xhr.open("GET", "proxy.php?term="+ input + "&" + "bounds=" + gbb + "&limit=10");
    xhr.setRequestHeader("Accept","application/json");
    xhr.onreadystatechange = function () {
      if (this.readyState == 4) {
        json = JSON.parse(this.responseText);
        var str = JSON.stringify(json,undefined,2);
        //document.getElementById("output").innerHTML = "<pre>" + str + "</pre>";
        restaurantInfo();
     }
 };
 xhr.send(null);
}

// addMarker function adds numbered markers on the map with respective to the restaurant found!
function addMarker(rest_add,count){
  var address = rest_add;
      geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location,
            icon: 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld='+ (count+1) +'|e74c3c|000000'
        });
        markers.push(marker);
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });

}
// removeMarker removes the marker from the map so as to add news markers for a new search!
function removeMarker(){
  if(markers.length>0){
   for (var i = 0; i < markers.length; i++) {
     markers[i].setMap(null);
   }
 } if(markers.length>0){
   for (var i = 0; i < markers.length; i++) {
     markers[i].setMap(null);
   }
 }
}

// restaurantInfo function print the information about the restaurant according to search. It also calls the addmarker function
function restaurantInfo() {
// Remove Marker--------------------------------------------
    removeMarker()
    var pd =document.getElementById("description");
    pd.innerHTML="";
    
    for (var i=0;i<json.businesses.length;i++){
      var rest_address = ""
      for (add in json.businesses[i].location.display_address){
        rest_address = rest_address + " " + json.businesses[i].location.display_address[add]
      }
      
    addMarker(rest_address,i);
//Get Data on left side--------------------------------------------

      var count = document.createElement("div")
      var linebreak = document.createElement('br');

      var restaurantImage =document.createElement("img");
      restaurantImage.src = json.businesses[i].image_url;
      
      var restaurantLink = document.createElement("a");
      restaurantLink.href = json.businesses[i].url;
      restaurantLink.innerHTML = (i+1)+ "." + json.businesses[i].name;
      restaurantLink.style.font="bold 20px calibri";

      var ratingImg =document.createElement("img");
      ratingImg.src =json.businesses[i].rating_img_url_large;
      

      var overview =document.createElement("div");
      overview.innerHTML = "Snippet Text: ".bold().fontsize(4) + (json.businesses[i].snippet_text).fontsize(4);
 
      pd.appendChild(restaurantImage);
      pd.appendChild(linebreak);
      pd.appendChild(count);
      pd.appendChild(restaurantLink);
      pd.appendChild(document.createElement("br"));
      pd.appendChild(ratingImg);
      pd.appendChild(linebreak);
      pd.appendChild(overview);
      pd.appendChild(linebreak);
      pd.appendChild(linebreak);

  }
}
google.maps.event.addDomListener(window, 'load', initialize);