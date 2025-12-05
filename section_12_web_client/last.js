
function last() {

 if (!(active)){
	 return;
 }

 playing=false;
 pb=document.getElementById('playButton');
 pb.value="Play";

 displayImage = document.getElementById('displayImage');
 image_index = image_urls.length - 1;
 displayImage.src = image_array[image_index].src;

 return;

}
