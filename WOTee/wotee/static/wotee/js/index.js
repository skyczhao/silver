/**
 * Copyright 2015 Tobin.
 *
 */

// check dependency
if (typeof jQuery === 'undefined') {
    throw new Error('The script "index.js" requires jQuery')
}

// main script
$(function() {
    // click to select image
    $("#preview").click(function() {
        $("#image").click();
    });

    // check preview function
    if (typeof FileReader === 'undefined') {
        // show the error message
        $("#message").addClass("text-danger");
        $("#message").html("your browser does not support the preview function");
        // change the way to select image
        $("#preview").addClass("hidden");
        $("#image").removeClass("hidden");
    } else {
        // change preview window after selecting
        $('#image').change(function() {
            var file = this.files[0];
            var reader = new FileReader();
            // read file
            reader.readAsDataURL(file);
            // loading
            reader.onload = function(e) {
                $("#preview").attr("src", this.result);
            }
        });
    }
});