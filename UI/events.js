async function submitRegistrationForm() {
    var fname = document.getElementById("fname");
    var lname = document.getElementById("lname");
    var login = document.getElementById("login");
    var email = document.getElementById("email");
    var ele = document.getElementsByName('gender');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            var genderSelect = ele[i].value;
        
    }
    
    if (genderSelect == "Male")
        var gender = 'M';
    else if (genderSelect == "Female")
        var gender = 'F';
    else var gender = 'O';
    
    let xhr = new XMLHttpRequest();

    let userCreateApi = "http://127.0.0.1:5000/api/users/add";

    xhr.open("POST", userCreateApi, false);

    xhr.setRequestHeader("Content-Type", "application/json");


    let data = JSON.stringify({
        "firstname": fname.value,
        "lastname": lname.value,
        "login": login.value,
        "email": email.value,
        "gender": gender
    });
    console.log(data);

    xhr.onload = () => console.log(xhr.responseText);
    try {
    xhr.send(data);
        if (xhr.status != 200) {
            alert(`Error ${xhr.status}: ${xhr.statusText}`);
        } else {

            let response = JSON.parse(xhr.responseText);
            alert(response.message);
        }
    } catch (err) { // instead of onerror
        alert("Request failed");
    }
}

function validateRegistrationForm() {
    var fname = document.getElementById("fname");
    var lname = document.getElementById("lname");
    var login = document.getElementById("login");
    if (fname.value == "") {
        alert("Please enter some value for First Name.");
        return;
    }
    if (lname.value == "") {
        alert("Please enter some value for Last Name.");
        return;
    }
    if (login.value == "") {
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