// let this get stuck first also
var ourLoc;
// this will get trapped in the previous function
// then note we have to now declare the view variable on the top
var view;

// i need this here last stop
var countryRequest;

// I don't think i need this here var map;

// Notes about LAYERS;
// Open Layer offers different types of layers. Layers are like
// different brushes used to make the same image. They look different.
// Some might take more time than others.

// TWO but, let's put all this logic in a function! Putting it in a function will make our code cleaner and it'll be easier for us to debug.
// a common name for the first thing you want to run is init, short for initilize. it's not a required name like in python. You can call it whatever you want but convention is init.
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
// We'll have to make a button in our html.
// generally we only want to put text in a p tag, but let's ignore that for now and for efficiency and the MVP let's just put it in a P tag.
// Now we need to access that same view variable outside of the INIT function!
// Any ideas on how to do that.
// And now we have to separate it in the init function as well!
function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000
  });
}
// new init function with it separated
// let's also separete the lon and lat, let's make it the bay area, yeah? does anyone know how to get that?
ourLoc = ol.proj.fromLonLat([41.043316, 28.862457]);

	view = new ol.View({
		center: ourLoc,
		zoom: 6
	});

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

// We have a map, it moves! But we can't search for new locaitons. GO BACK TO SLIDES. talk about rest for a while

// FOUR great, let's add an input field in the HTML, and a button to submit the value in that input field.
// Let's make a new function to hold this logic

function panToLocation() {
	// Let's grab that input element off the DOM
  // And then let's grab the value of what's inside the input. It's really just dotnoation.value
	var countryName = document.getElementById("country-name").value;

	// Let's add an error check to make sure
	// the person has typed something in.
	if(countryName === "") {
	 	alert("You didn't enter a country name!");
	 	return;
  }

  // Cool it tells us to put the name of the country into this URL... but then what?
	var query = "https://restcountries.eu/rest/v2/name/"+countryName
}


// FIVE Let's do this get request! There are multiple ways to do this, and today we're going to do it with XML requests. Let's google XML request
function panToCountry() {
	var countryName = document.getElementById("country-name").value;

	var query = "https://restcountries.eu/rest/v2/name/"+countryName

  // do this last, the error check
	query = query.replace(/ /g, "%20")
	alert(query);

	// Step 1: Let's start by making an HTTP GET request:
	var countryRequest = new XMLHttpRequest();
	countryRequest.open('GET', query, false);

	// Step 2: Send the request and see the output:
	countryRequest.send();
  // Let's do this with alerts to make sure everyone can see it clearly. You can of course do this as a console.log
	alert("Ready State " + countryRequest.readyState);
	alert("Status " + countryRequest.status);
	alert("Response" + countryRequest.responseText);

  // NOW SHOW THEM THE RESPONSE TEXT CONSOLE.LOGGED
  // That is super hard to understand right?
  //
	// Note: If you run into an error like window
	// not loading, check that you declared VAR
	// before the location variable.

}





// TWO this will call init when the window is loaded.
window.onload = init
