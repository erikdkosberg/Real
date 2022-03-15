This text editor works by setting the contenteditable flag on the content div.

JS can set a function to run on an interval (using 'setInterval(function() {...}, 1000);')

Before starting the loop,

We initialize the .innerHTML attribute, and set localStorage["text"] as its value.

Now every time we try to get the innerHTML it gives is whatever is is localStorage.

Meaning we just need to update the localStorage to the value of the innerHTML,
which really is just recursively calling the localStorage.

What's really cool about this way of doing it, is that it allows us to access one
div at any point in time to get the content.

We could have some options for settings to configure the editor, like custom font and
spacing etc.

I'm not exactly sure if there are any safety implications of the contentEditable flag, but it might
be worth noting that it allows you to change anything on the page (not sure why this would 
necessarily be a problem)

