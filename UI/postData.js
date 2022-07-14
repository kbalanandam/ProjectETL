function submitRegistrationForm() {
    var user = document.getElementById("user");
    var email = document.getElementById("email");
    const response = await fetch("http://127.0.0.1:5000/api/users/add", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: `{
   "name": user,
   "email": email
  }`,
    });

    response.json().then(data => {
        console.log(data);
    }
    };
