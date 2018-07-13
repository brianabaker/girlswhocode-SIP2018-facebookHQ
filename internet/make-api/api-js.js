var view;
var ourLoc;
var countryRequest;

function init(){
  ourLoc = ol.proj.fromLonLat([-122.147066, 37.481155])

  view = new ol.View({
    center: ourLoc,
    zoom: 6
  });

  var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  ],
  view: view
  });
}

function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000
  });
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;

  var query = "https://restcountries.eu/rest/v2/name/" + countryName + "?fullText=true"

  countryRequest = new XMLHttpRequest();

  countryRequest.open("GET", query, true);
  countryRequest.send();

  countryRequest.onload = processCountryRequest;
}

function processCountryRequest(){
  var cleanedResponse = JSON.parse(countryRequest.responseText)

  if(countryRequest.readyState != 4 || countryRequest.status != 200){
    alert('Error');
    return;
  }
  var lat = cleanedResponse[0].latlng[0]
  var lon = cleanedResponse[0].latlng[1]
  var location = ol.proj.fromLonLat([lon, lat])

  view.animate({
    center: location,
    duration: 2000
  });
}





window.onload = init
