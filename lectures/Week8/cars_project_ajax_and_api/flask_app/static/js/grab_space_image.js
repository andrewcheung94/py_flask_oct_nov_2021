window.addEventListener('load', () => { // Arrow function: (e, x) => {} is equivalent to function(e, x) {}
    let space_form = document.getElementById("space_image_form");
    space_form.addEventListener("submit", function(e) {
        e.preventDefault(); // Stop the browser from going to that route by default when the form is submitted
        console.log("Submitted");
        let form = new FormData(space_form);
        // this how we set up a post request and send the form data.
        fetch("http://localhost:5000/search_space_images", {method: 'POST', body: form})
            .then( response => response.json() ) // Convert the response sent from the jsonify() method into json data
            .then( data => {
                // console.log(data);
                let output_spot = document.getElementById("space_placeholder");
                if (data.message != undefined) { // No date entered, so message key would exist
                    output_spot.innerHTML = "<p>No date entered</p>";
                } else { // Date entered, so show image
                    let output_spot = document.getElementById("space_placeholder");
                    output_spot.innerHTML = `<img src="${data.url}">`;
                    // Code below does NOT work
                    // let image_element = document.createElement("img");
                    // image_element.setAttribute("src",data.url);
                    // output_spot.appendChild(image_element);
                }
            })
    })
})
