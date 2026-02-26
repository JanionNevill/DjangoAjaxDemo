$(document).ready(
    function(){
        // Function to clear outputs
        function clearOutput(){
            $("#index-p")[0].innerHTML = "";
            $("#number-p")[0].innerHTML = "";
            $("#sequence-p")[0].innerHTML = "";
        };

        // Clear outputs when submit button clicked
        $("#fibonacci-btn").on(
            "click",
            clearOutput
        );

        // Run AJAX update when valid form submitted
        $("#fibonacci-form").on(
            "submit",
            function(){
                // Clear output if form invalid
                if (!$("#fibonacci-form")[0].reportValidity()) {
                    return;
                }

                // Disable button and show spinner
                $("#fibonacci-btn")[0].disabled = true;
                $("#spinner-div")[0].innerHTML = '<div class="lds-dual-ring"></div>';
                // AJAX post request to get Fibonacci numbers up to the given index
                // Runs in the background, then updates the page
                $.ajax({
                    url: form_demo_url,
                    type: "post",
                    // Add the CSRF token to the form data
                    data: {
                        ...{"csrfmiddlewaretoken": csrf_token},
                        ...Object.fromEntries(new FormData($("#fibonacci-form")[0]))
                    },
                    success: function(data) {
                        // Enable the button and hide the spinner
                        $("#fibonacci-btn")[0].disabled = false;
                        $("#spinner-div")[0].innerHTML = "";
                        // Replace the output with the response from the server
                        $("#index-p")[0].innerHTML = "Index: " + data.index;
                        $("#number-p")[0].innerHTML = "Number: " + data.number;
                        $("#sequence-p")[0].innerHTML = "Sequence: " + data.sequence;
                    },
                    failure: function(data) {
                        alert("Got an error dude");
                    }
                });
            }
        );
    }
)