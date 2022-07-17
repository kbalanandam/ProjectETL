// api url
const api_url =
	"http://127.0.0.1:5000/api/users";

// Defining async function
async function getapi(url) {

	// Storing response
	const response = await fetch(url);

	// Storing data in form of JSON
	var data = await response.json();
	console.log(data);
	if (response) {
		hideloader();
	}
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
	let tab =
		`<tr>
			<th>UserId</th>
			<th>First Name</th>
			<th>Last Name</th>
			<th>Gender</th>
			<th>login</th>
			<th>Email</th>
			<th>Inactive</th>
		</tr>`;
	
	// Loop to access all rows
	for (let r of data.users) {
		tab += `<tr>
			<td>${r.id} </td>
			<td>${r.firstname} </td>
			<td>${r.lastname} </td>
			<td>${r.gender} </td>
			<td>${r.login}</td>
			<td>${r.email}</td>
			<td><input type="checkbox"></td>
		</tr>`;
	}
	// Setting innerHTML as tab variable
	document.getElementById("users").innerHTML = tab;
}
// JavaScript source code
