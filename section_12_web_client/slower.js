
function slower() {

 if (!(active)){
	 return;
 }

 if (wait_time < 1000){
  wait_time = 3.0*wait_time/2.0;
 } else {
  alert("Minimum speed reached");
 }

 return;

}
