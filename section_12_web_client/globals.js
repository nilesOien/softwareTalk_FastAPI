// Global variables
var active=false;             // True if buttons should be active (images loaded)
var playing=false;            // True if we are advancing images
var image_array = Array();    // Array of images
var image_urls = Array();     // Array of urls
var image_index = 0;          // Index of current image
var image_increment_sign = 1; // Image increment sign
var image_increment_mag = 1;  // Image increment magnitude
var num_loaded = 0;           // How many images have we loaded
var wait_time = 50;           // Delay in playing.
