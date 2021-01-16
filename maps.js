// Using Leaflet

var lat = 51.505;
var lng = -0.09;
var zoomLevel = 13;
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
    zoomOffset: -1,
    accessToken: 'your.mapbox.access.token'
}).addTo(map);

setTimeout(() => {
  map.flyTo([50, 10], zoomLevel);
}, 2000);
