
function cadence() {

 if (!(active)) return;

 let cb = document.getElementById('cadenceBox');
 let cText = cb.value;
 ci = parseInt(cText, 10); 
 if (isNaN(ci)){
  alert("Invalid cadence : " + cText);
  return;
 }

 if (ci < 1){
  alert("Invaid value : " + cText);
  return;
 }

 image_increment_mag = ci;

 return;
}
