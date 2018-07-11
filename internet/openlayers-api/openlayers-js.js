// let this get stuck first also
var ourLoc;
// this will get trapped in the previous function
// then note we have to now declare the view variable on the top
var view;
var map;

// Open Layer offers different types of layers. Layers are like
// different brushes used to make the same image. They look different.
// Some might take more time than others.

function init(){
  ourLoc = ol.proj.fromLonLat([-122.155872, 37.482087])
  // i declared the variable at the top, so now i can use it here

  view = new ol.View({
    center: ourLoc,
    zoom: 4
  })

  map = new ol.Map({
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
  var countryName = document.getElementById("country-name").value

  if (countryName === "") {
    alert("You didn't enter a country name!")
    return;
  }

  var query = "https://restcountries.eu/rest/v2/name/" + countryName
  console.log(query)
}


window.onload = init
