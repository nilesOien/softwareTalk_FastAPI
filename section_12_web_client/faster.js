
function faster() {

 if (!(active)){
	 return;
 }

 if (wait_time > 10){
  wait_time=2.0*wait_time/3.0;
 } else {
  alert("Maximum speed reached");
 }

 return;

}
