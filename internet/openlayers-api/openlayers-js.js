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

function synchonousPanToLocation(){
  var countryName = document.getElementById("country-name").value

  if (countryName === "") {
    alert("You didn't enter a country name!")
    return;
  }

  var query = "https://restcountries.eu/rest/v2/name/" + countryName
  console.log(query)

  // let's do another error control. URLS can't contain spaces, so we need to convert spaces to the symbol for a space, %20. we can use regex for this.

  query = query.replace(/ /g, "%20")
  console.log(query)

  // cool the docs say to create an object. let's do that.
  var countryRequest = new XMLHttpRequest()
  countryRequest.open("GET", query, false);

  countryRequest.send()
  // i want to make sure everyone sees this, so let's make it alerts for now

  // alert("Ready state" + countryRequest.readyState)
  // alert("Status" + countryRequest.status)
  // alert("Response " + countryRequest.responseText)

 // part 6
 // first let's make sure we only pan if information is correct

   if (countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === ""){
   console.log("Request had an error")
   return
 }

// we need to grab that information. show them what it looks like without JSON.parse
 	var countryInformation = JSON.parse(countryRequest.responseText)

// now let's grab the lat and lon
  var lat = countryInformation[0].latlng[0]
  var lon = countryInformation[0].latlng[1]

// sweet! we have that information now. let's pan to view at that lat + lng
  var location = ol.proj.fromLonLat([lon, lat])

  view.animate({
    center: location,
    duration: 2000
  })
// awesome! we got it!
// now let's take another look at this console warning.
// who knows the word deprecated?
// awesome let's look at it together on wikipedia.
// definition  deprecation is the discouragement of use of some terminology, feature, design, or practice, typically because it has been superseded or is no longer considered efficient or safe, without completely removing it or prohibiting its use.
} // end synchronous pan to location

function asynchonousPanToLocation(){
  var countryName = document.getElementById("country-name").value

  if (countryName === "") {
    alert("You didn't enter a country name!")
    return;
  }

  var query = "https://restcountries.eu/rest/v2/name/" + countryName

  query = query.replace(/ /g, "%20")

  countryRequest = new XMLHttpRequest()
  // so let's make this async! change the get request async option to "true"

  countryRequest.open("GET", query, true);

  countryRequest.onload = processCountryRequest

  countryRequest.send()

// let's organize the rest of this code in a different function
}

function processCountryRequest(){
    if (countryRequest.readyState != 4 || countryRequest.status != 200 || countryRequest.responseText === ""){
      alert("We were unable to find your requested country!")
      return
    }

 	var countryInformation = JSON.parse(countryRequest.responseText)

  var lat = countryInformation[0].latlng[0]
  var lon = countryInformation[0].latlng[1]

  var location = ol.proj.fromLonLat([lon, lat])

  view.animate({
    center: location,
    duration: 2000
  })

}




window.onload = init
