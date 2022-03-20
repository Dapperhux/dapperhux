function peter() {
	var eds = 0;
	var number = document.getElementById('body');
	eds = number.value.length;
    if (number.value.length < 6) {
    	alert("INPUT VALIT TIPS BEFORE POST");
    	return false;
    }
}