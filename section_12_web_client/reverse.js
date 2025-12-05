
function reverse() {

 if (!(active)){
	 return;
 }
 db=document.getElementById('dirButton');
 image_increment_sign = -1 * image_increment_sign;

 if (image_increment_sign > 0){
  db.value='Reverse';
 } else {
  db.value='Forward';
 }

 return;

}
