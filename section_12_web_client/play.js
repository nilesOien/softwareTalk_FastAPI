// We go here when the play button is clicked.
function play() {

 if (!(active)){
	 return;
 }

 pb=document.getElementById('playButton');
 if (playing){
  playing=false;
  pb.value="Play";
 } else {
  playing=true;
  pb.value="Stop";
 }

 if (playing){
  advance_image();
 }

 return;

}

// Internal function to advance the displayed image to the next one.
function advance_image(){

 if (!(active)) return;
 if (!(playing)) return;

 let next_index = image_index + image_increment_sign * image_increment_mag;

 if (next_index < 0){
  next_index = num_loaded - 1;
 }

 if (next_index > num_loaded - 1){
  next_index = 0;
 }

 // Display the image and set the index.
 displayImage = document.getElementById('displayImage');
 displayImage.src = image_array[next_index].src;
 image_index=next_index;

 // Update the image progress bar.
 let ipBar = document.getElementById('imageProgressBar');
 ipBar.value = image_index;

 console.log("Displaying image " + image_index + " of " + num_loaded);

 // Call this function again after a delay.
 setTimeout(advance_image, wait_time);

 return;

}
