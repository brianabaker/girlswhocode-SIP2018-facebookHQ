document.addEventListener("DOMContentLoaded", function() {
  console.log("LOADED")

  // alert("Hi Hi Hi Hi Hi Hi Hi Hi Hi Hi Hi")
  let changeColorLink = document.getElementById("change-color")
  let personalPhoto = document.getElementById("personal-photo")
  let toggle = 0

  changeColorLink.addEventListener('click', changeColor)

  personalPhoto.addEventListener('click', function() {
    console.log("in the change photo");
    console.log(personalPhoto.src);
    if (personalPhoto.src == "file:///Users/flatironschool/Development/girlswhocode/internet/my-about-me/backpack.jpg") {
      personalPhoto.src = "flowers-crown.png"
    } else if (personalPhoto.src == "file:///Users/flatironschool/Development/girlswhocode/internet/my-about-me/flowers-crown.png") {
      personalPhoto.src = "small-cast.png"
    } else {
      personalPhoto.src = "backpack.jpg"
    }
  })

  function changeColor(){
    if (toggle == 0) {
      document.body.style.color = "purple";
      document.body.style.backgroundColor = "antiquewhite"
      toggle = 1
    } else if (toggle == 1) {
      document.body.style.color = "pink";
      document.body.style.backgroundColor = "black"
      toggle = 2
    } else if (toggle == 2) {
      document.body.style.color = "cyan";
      document.body.style.backgroundColor = "darkred"
      toggle = 3
    } else if (toggle == 3) {
      document.body.style.color = "black";
      document.body.style.backgroundColor = "lavender"
      toggle = 0
    }
  }



}) // END OF DOM CONTENT LOADED
