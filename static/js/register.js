function james() {
	var email1 = document.getElementById('email11');
	var email12 = document.getElementById('email2');
	if (email1.value != email12.value) {
		alert("the two emails must match!!");
		return false;
	}
}


function johns() {
	var password11 = document.getElementById('password');
	var password22 = document.getElementById('password2');
	if (password11.value != password22.value) {
		alert("the two password must match!!");
		return false;
	}
}

function peter() {
	var eds = 0;
	var number = document.getElementById('phone_number');
	eds = number.value.length;
    if (number.value.length != 11) {
    	alert("PLEASE INSERT YOUR PHONE NUMBER CORRECTLY !!!");
    	return false;
    }
}