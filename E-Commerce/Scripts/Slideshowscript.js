//  S L I D E S H O W   S C R I P T


 // Core script which changes slide either to the next or previous slide
var slideIndex = 1;
sSlides(slideIndex);

function pSlides(n) {
  sSlides(slideIndex += n);
}

function cSlide(n) {
  sSlides(slideIndex = n);
}

//Slide show elements Scrip
function sSlides(n) {
  var i;
  var slides = document.getElementsByClassName("Slides");
  var dots = document.getElementsByClassName("dems");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}

//W3 School tutorial