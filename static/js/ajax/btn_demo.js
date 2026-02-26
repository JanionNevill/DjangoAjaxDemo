$(document).ready(
    function(){
        var clicks = 0;

        $("#fibonacci-btn").click(
            function(){
                clicks += 1;

                // Clear outputs
                $("#index-p")[0].innerHTML = "";
                $("#number-p")[0].innerHTML = "";
                $("#sequence-p")[0].innerHTML = "";

                // Disable button and show spinner
                $("#fibonacci-btn")[0].disabled = true;
                $("#spinner-div")[0].innerHTML = '<div class="lds-dual-ring"></div>';
                // AJAX post request to get Fibonacci numbers up to the given index
                // Runs in the background, then updates the page
                $.ajax({
                    url: btn_demo_url,
                    type: "post",
                    // Add the CSRF token and number of clicks to the form data
                    data: {
                        "csrfmiddlewaretoken": csrf_token,
                        "index": clicks
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