// Small function called when we load an image.
// Advances the progress bar.
function loadedImage(){

 num_loaded++;
 let percentDone = (100.0*num_loaded/image_urls.length).toFixed(2);
 console.log("Loaded image " + num_loaded + " of " + image_urls.length + " (" + percentDone + "%) " + `${this.src}`);

 let pBar = document.getElementById('loadProgressBar');
 pBar.value=num_loaded;

 // If it's the first image loaded, then it's the
 // last in the time sequence because we loaded
 // backwards, so display it, and set the index.
 if (num_loaded == 1){
  displayImage = document.getElementById('displayImage');
  image_index = image_urls.length - 1;
  displayImage.src = image_array[image_index].src;
 }

 // If it's the last image, activate the buttons.
 // Also set up image progress bar.
 if (num_loaded == image_urls.length){
  active=true;
  let ipBar = document.getElementById('imageProgressBar');
  ipBar.max=num_loaded;
  ipBar.value=num_loaded;
  console.log("Completed load of " + image_urls.length + " images");
 }

 return;
}


// We call this function when the load button is clicked.
// Assembles the FastAPI URL to get the image list from and calls it.
async function load() {

 active=false;
 playing=false;
 pb=document.getElementById('playButton');
 pb.value="Play";

 num_loaded=0;

 // url is something like this :
 // "http://localhost:8000/database-dict?minTime={args.minTime}&maxTime={args.maxTime}&siteCSV={args.siteCSV}" 

 let startTime=document.getElementById('startBox').value;
 let endTime  =document.getElementById('endBox').value;
 url="http://localhost:8000/database-dict?minTime=";
 url = url + startTime;
 url = url + "&maxTime=" + endTime;

 let sites=document.getElementById('sitesBox').value;
 if (sites.length > 0){
  url = url + "&siteCSV=" + sites;
 }

 console.log("Fetching image list from FastAPI server URL " + url);

 // Get data from the server.
 let problemLoading=false;
 let response = await fetch(url).catch(error => {
  console.log(error.message);
  alert("Failed to fetch list (is the server running?)");
  problemLoading=true;
  return;
 });

 if (problemLoading){
  return;
 }

 if (response.status != 200) {
  alert(response.statusText);
  return;
 }

 let data = await response.text();
 let reply=JSON.parse(data);

 // Load the URLs into image_urls, and make the
 // adjustment so that they point to images rather than
 // data files.
 image_urls = Array();
 for (i=0; i < reply.length; i++){
  image_urls[i] = reply[i].url;
  image_urls[i] = image_urls[i].replace(/haf/g, "hac");
  image_urls[i] = image_urls[i].replace(/fits.fz/g, "jpg");
 }

 // Set the load progress bar to 0.
 let pBar = document.getElementById('loadProgressBar');
 pBar.max=reply.length;
 pBar.value=0;

 // Load images backwards so we get the last image first.
 image_array = Array(image_urls.length);
 for(var i = image_urls.length - 1; i > -1; i--) {
  image_array[i] = new Image();
  image_array[i].onload=loadedImage;  // Call loadedImage() when we load an image.
  image_array[i].src = image_urls[i]; // This starts the image load.
  console.log("Initiating loading of image " + image_urls[i]);
 }

 console.log("-- End of image load initiation --");

 return;

}
