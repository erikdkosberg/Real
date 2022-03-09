
document.write("Welcome to the localhost");
document.write("<br/> <br/>");

// Master Dictionary to pass between Python and JS
var data = {};

// Initialize attributes on the main page
function init_page() {
    
    document.body.setAttribute("bgColor", "cyan");
};

// Discrete function calls go here; only called once
init_page();
		

window.addEventListener('load', init_page);