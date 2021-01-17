// Using Leaflet

var lat = imageData[0][0][0];
var lng = imageData[0][0][1];
var zoomLevel = 17;
var map = L.map("mapid", {
  center: [lat, lng],
  zoom: zoomLevel,
  scrollWheelZoom: false,
  zoomControl: false
});
map.dragging.disable();
map.touchZoom.disable();
map.doubleClickZoom.disable();
map.scrollWheelZoom.disable();
map.boxZoom.disable();
map.keyboard.disable();
if (map.tap) map.tap.disable();
document.getElementById("mapid").style.cursor = "default";

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYWthcG9vcjIwMiIsImEiOiJja2swM2QyemQwOGtzMm9udDc4ZTFjd2lmIn0.eigfIGqGRuxYOO3ZpLmKsA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(map);

function movement(image) {
  map.flyTo(image[0], zoomLevel);
  var img = new Image();
  img.src = image[2];
  img.alt = image[3];
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  var captionText = document.getElementById("caption");
  modal.style.display = "block";
  modalImg.src = img.src;
  captionText.innerHTML = img.alt;
  // modalImg.onload = function() {
  //   if (this.height > this.width) {
  //     var newHeight = window.innerHeight * 0.75;
  //     this.width = newHeight / this.height * this.width;
  //     this.height = newHeight;
  //   } else {
  //     var newWidth = window.innerWidth * 0.75;
  //     this.height = newWidth / this.width * this.height;
  //     this.width = newWidth;
  //   }
    // if(this.height > window.innerHeight-50 || this.width > window.innerWidth-50) {
    //   this.height *= 0.75;
    //   this.width *= 0.75;
    //   console.log(this.height, this.width);
    // }
  // }
  setTimeout(() =>{
    modal.style.display = "none";
  }, 3000);
}

imageData.forEach((image, i) => {
  var imageIcon = L.icon({
    iconUrl:  "/static/thumbnails/" + image[1][0],
    iconSize: [40/image[1][2]*image[1][1], 40]
  })
  L.marker(image[0], {icon:imageIcon}).addTo(map);
  if(i == 0) {
    movement(image);
  } else {
    setTimeout(() => {
      movement(image);
    }, 5000*i);
  }
});
