function validateRegistrationForm() {
    var fname = document.getElementById("fname");
    var lname = document.getElementById("lname");
    var user = document.getElementById("user");
    if (fname.value == "") {
        alert("Please enter some value for First Name.");
        return;
    }
    if (lname.value == "") {
        alert("Please enter some value for Last Name.");
        return;
    }
    if (user.value == "") {
        alert("Please enter user name to register.");
        return;
    }
    
}

function validateLoginForm() {
    var loginname = document.getElementById("loginname");
    
    if (loginname.value == "") {
        alert("Please enter login details.");
        return;

    }
    var password = document.getElementById("pass");
    if (password.value == "") {
        alert("Please enter password.");
        return;

    }
}