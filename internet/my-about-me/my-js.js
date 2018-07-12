


document.addEventListener("DOMContentLoaded", function() {

  // alert("Hello World!");
  // console.log("JEUUUU");

  let myPhoto = document.getElementById("personal-image")

  // myPhoto.addEventListener("click", changeImage)


  function changeImage(){
    // console.log('HEYYYY');
    console.log(myPhoto.src);
    if (myPhoto.src == "file:///Users/facebook/development/girlswhocode-SIP2018-facebookHQ/internet/my-about-me/backpack.jpg") {
      myPhoto.src = "flowers-crown.png"
    } else {
      myPhoto.src = "backpack.jpg"
    }
  }


}) // END OF DOM CONTENT LOADED
