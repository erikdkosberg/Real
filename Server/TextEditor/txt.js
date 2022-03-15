
// Initialize the divs; set innerHTML to lookup whatever is in localStorage
document.getElementById("heading").innerHTML = localStorage["title"] || "Just Write"; // default text
document.getElementById("content").innerHTML = localStorage["text"] || "This text is automatically saved every second"; 

// Not actually doing anything, purely demonstrational
// These both do the same thing; the content is both in local storage and the html page
const meth1 = document.getElementById("content").innerHTML;
const meth2 = window.localStorage.getItem('text');

function getContent () {
    /*
    Sets the local storage to whatever is currently in the content div
    */

  localStorage["title"] = document.getElementById("heading").innerHTML; // heading div
  localStorage["text"] = document.getElementById("content").innerHTML; // content div
}
setInterval(getContent(), 1000);