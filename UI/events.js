async function submitRegistrationForm() {
    var user = document.getElementById("user");
    var email = document.getElementById("email");
    let xhr = new XMLHttpRequest();

    xhr.open("POST", "http://127.0.0.1:5000/api/users/add");

    xhr.setRequestHeader("Content-Type", "application/json");


    let data = JSON.stringify({
        "name": user.value,
        "email": email.value
    });
    console.log(data);

    xhr.onload = () => console.log(xhr.responseText);

    xhr.send(data);
}

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
    submitRegistrationForm()
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