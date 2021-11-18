// window.onload = (e) => { // Arrow function: (e, x) => {} is equivalent to function(e, x) {}
window.addEventListener('load', () => {
    let manu_form = document.getElementById("manufacturer_form");
    manu_form.addEventListener("submit", function(e) {
        e.preventDefault(); // Stop the browser from going to that route by default when the form is submitted
        console.log("Submitted");
        let form = new FormData(manu_form);
        // this how we set up a post request and send the form data.
        fetch("http://localhost:5000/search_manufacturers", {method: 'POST', body: form})
            .then( response => response.json() ) // Convert the response sent from the jsonify() method into json data
            .then( data => {
                // console.log(data);
                // Where we will put the results from the search
                let output_spot = document.getElementById("search_results");
                output_spot.innerHTML = ""; // Clear the search results
                if (data.length == 0) { // None found
                    output_spot.innerText = "No manufacturer found";
                } else { // At least one found
                    let new_list = document.createElement("ul"); // Create an unordered list
                    // Loop to grab the results, one by one
                    for (let k = 0; k < data.length; k++) {
                        // Output: <li><a href="/manufacturers/<id_num>">Name of manufacturer</a></li>
                        let current_row = data[k];
                        let new_item = document.createElement("li");
                        let new_link = document.createElement("a");
                        new_link.innerText = current_row.name; // Put in name of manufacturer
                        new_link.setAttribute("href","/manufacturers/"+current_row.id);
                        new_item.appendChild(new_link);
                        new_list.appendChild(new_item); // Add item to the list
                    }
                    output_spot.appendChild(new_list); // Add list to the HTML at last
                }
            })
    })
})

// // Second version with "onsubmit"
// window.onload = e => {
//     let manu_form = document.getElementById("manufacturer_form");
//     // console.log(manu_form)
//     manu_form.onsubmit = function(e) {
//         e.preventDefault();
//         let form = new FormData(manu_form);
//         fetch("http://localhost:5000/search_manufacturers", { method:'POST', body: form})
//             .then( response => response.json() )
//             .then( data => {
//                 let results_location = document.getElementById("search_results");
//                 results_location.innerHTML = ""; // Clear results
//                 console.log(data);
//                 if (data.length == 0) {
//                     results_location.innerHTML = "Manufacturer not found";
//                 } else {
//                     // Build table
//                     let new_list = document.createElement("ul");
//                     for (var k = 0; k < data.length; k++) {
//                         // Add rows to the table here
//                         let currentManufacturer = data[k];
//                         let new_item = document.createElement("li");
//                         let new_link = document.createElement("a");
//                         new_link.setAttribute("href","/manufacturers/"+currentManufacturer.id);
//                         new_link.innerText = currentManufacturer.name;
//                         new_item.appendChild(new_link);
//                         new_list.appendChild(new_item);
//                     }
//                     results_location.appendChild(new_list);
//                 }
//             })
//     }
// }