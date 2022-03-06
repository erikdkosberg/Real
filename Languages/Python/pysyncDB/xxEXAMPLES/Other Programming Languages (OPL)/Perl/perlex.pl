=cut
This is
a multiline comment
=cut    

# whitespaces are ignored
use strict;
use warnings FATAL => 'all';
print "Hello
world\n";

#prints everything in between <<FOO and FOO
print <<FOO;
Four score and seven years ago
our fathers set onto this continent
(keep going here ...\n)
FOO

# Scalars are any variable that can be represented with one value

my $animal = "camel";
my $answer = 42;

print "$animal\n";
print "The animal is $animal\n";
print "The square of $answer is ", $answer * $answer, "\n";

#print;

# Arrays are a one dimensional list of items

my @animals = ("camel", "llama", "owl");
my @numbers = (23, 42, 69);
my @mixed   = ("camel", 42, 1.23);

print $animals[0];              # prints "camel"
print $animals[1];              # prints "llama"
print "$mixed[$#mixed]\n";      # last element, prints 1.23

# Getting multiple values from an array

print "@animals[0,1]\n";                 # gives ("camel", "llama");
print "@animals[0..2]\n";                # gives ("camel", "llama", "owl");
print "@animals[1..$#animals]\n";        # gives all except the first element

my @sorted    = sort @animals;
my @backwards = reverse @numbers;

my $size = @sorted;

print "hello $size";

@array = (1,2,3);
$array[50] = 4;

$size = @array;
$max_index = $#array;

print "Size:  $size\n";
print "Max Index: $max_index\n";

# Hashes are key-value pairs

my %fruit_color = ("apple", "red", "banana", "yellow");

# You can use whitespace and the => operator to lay them out more nicely:

my %fruit_color = (
    apple  => "red",
    banana => "yellow",
);
      
$fruit_color{"apple"};           # gives "red"

my @fruits = keys %fruit_color;
my @colors = values %fruit_color;

my $variables = {
    scalar  =>  {
                 description => "single item",
                 sigil => '$',
                },
    array   =>  {
                 description => "ordered list of items",
                 sigil => '@',
                },
    hash    =>  {
                 description => "key/value pairs",
                 sigil => '%',
                },
};

print "Scalars begin with a $variables->{'scalar'}->{'sigil'}\n";

# Variable Scoping
my $x = "foo";
my $some_condition = 1;
if ($some_condition) {
    my $y = "bar";
    print $x;           # prints "foo"
    print $y;           # prints "bar"
}
print $x;               # prints "foo"
print $y;               # prints nothing; $y has fallen out of scope

print "\n";

# If statements
$test = 1;
if ( $test == 1 ) {
    print "test 1";
} elsif ( $test == 2 ) {
    print "test 2";
} else {
    print "no test";
}

print "\n";

# If not statements
unless ( $test == 2 ) {
    print "were good here";
}

print "\n";

# the traditional way

if ($zippy) {
    print "Yow!";
}

# the Perlish post-condition way

print "Yow!" if $zippy;
print "We have no bananas" unless $bananas;

my $count = 1;
while ( $count < 5 ) {
    $count += 1; 
}

my $count = 1;
until ( $count == 3 ) {
    $count = "YAY";
    $count += 1; 
}
print($count);

for ($i = 0; $i <= $3; $i++) {
    print("looping");
}

foreach (@array) {
    print "This element is $_\n";
}

print $list[$_] foreach 0 .. $max;

# you don't have to use the default $_ either...
foreach my $key (keys %hash) {
    print "The value of $key is $hash{$key}\n";
}