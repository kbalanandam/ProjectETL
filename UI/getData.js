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
			<th>Name</th>
			<th>Email</th>
		</tr>`;
	
	// Loop to access all rows
	for (let r of data.users) {
		tab += `<tr>
			<td>${r.id} </td>
			<td>${r.name}</td>
			<td>${r.email}</td>
		</tr>`;
	}
	// Setting innerHTML as tab variable
	document.getElementById("users").innerHTML = tab;
}
// JavaScript source code
