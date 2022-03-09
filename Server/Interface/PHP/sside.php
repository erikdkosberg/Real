<h1>My User Web Root</h1>
<?php

// Print something to the screen
echo getcwd();

// Read the contents of a file
print_r(file("test.txt"));

// Open file for writing
$file = fopen("test.txt","w");

// Returns the number of bytes written
echo fwrite($file,"Hello World. Testing!");
fclose($file);

$command = 'ls';
exec($command, $out, $status);

echo "<br/> Example of a system call listing current dir here<br/>";
foreach($out as $dir){
	echo $dir;
	echo "<br/>";
}
?>
