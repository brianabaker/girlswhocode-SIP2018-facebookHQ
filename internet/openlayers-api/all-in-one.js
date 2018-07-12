// let this get stuck first also
var ourLoc;
// this will get trapped in the previous function
// then note we have to now declare the view variable on the top
var view;
var map;
var countryRequest;

// Open Layer offers different types of layers. Layers are like
// different brushes used to make the same image. They look different.
// Some might take more time than others.

// TWO but, let's put all this logic in a function!
function init(){
  var map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    view: new ol.View({
    center: ol.proj.fromLonLat([37.41, 8.82]),
    zoom: 4
    })
  });
}

// THREE let's add a pan to home ability.
// We'll have to make a button in our html
function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000
  });
}




// TWO this will call init when the window is loaded.
window.onload = init
