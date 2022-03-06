"""
Welcome to Penguin:

This script will allow you to easily parse in Python using lightweight and easily scalable modules.

For this example,
	
	We will be parsing through a text file and some html.
	The main() function will be used in a class called 'Parser'.
	We can look through our html with faster retrievals and less code
	by using list enumeration to generate any relevant index data
	as well as lambda functions to directly return function calls.
	
	***********************************************************************
	*		_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	 	*             
	*																																			*      
	*		please note that in python, capitalized letters are very SPECIFIC	*
	*		naming convention for variables should be considered as:         	*
	*		_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_	_							*
	*	       																															*	
	***********************************************************************
	
"""
naming_convention = {'func' : "my_function", #or function
	'class' : "Class", #class for subclass
	'variable' : "variable", #or "My_Variable"
	'list' : "my_list",
	'set' : "my_set",
}
"""

	This script was written and tested on Pythonista, with the intention
	to deploy with jupyter notebook.

	Let's start with confirming the path and using metclasses to hook into any attributes we might want to verify the conditions of. If and when a certain constraint might not be upheld, we can use a try statement to handle those errors accordingly. All additional modules can be imported and verified here:
		
	Loop through the naming convention to populate some data in case we
	might want to store, as well as provide direct access to the metaclass and error handler. 
	
	
"""
import sys
import os
import test

test.stack_check() #print("Path:	 " + os.path.dirname(__file__))

"""
class Meta(type()):
	def __init__(self):
		self.name = "Home Base"
	def error_handler():	
		try: self
		except NameError:
			pass
"""

#Global Functions

#link to naming conventions to build data types		
def key_seeker(naming_convention):
	for x in range(len(naming_convention.items())):
		key_list = [value for key, value in naming_convention.items()]
		
#new line shortcut
n = lambda : print('\n')
n()

#print lines shortcut
pl = lambda x:	print(lines)

"""
#catch = key seeker using list enumeration and a lambda function

The way this reads is that when you call this lambda function with argument y,
that key is used to search through 'the_list' looking for matching values.

This is the equivalent of using the def key_seeker(): syntax but actually
a faster way of doing it that uses less lines.

We can call x looking for y returned as z, caught in our variable 'catch' 

"""
the_list = [1,2,3]
catch = lambda x, y : [z for z in x if z == y]
print('Seeker:	' + str(catch(the_list, 3)))

n()

"""
	Phew.
	
	Okay, now we can define our mainloop() which inherits important qualities from class Parser(kwargs).
				
	There are two main classes, Parser and main:
		Since main() is the final line of the program, we are going to
		use this class to initialize our attributes for both of our
		classes by actually calling an instance or Parser() within main()
		
	We can bootstrap additional modules using subclasses within Parser i.e.
					Parser.html.some_new_function()
					
	Basic Functions:
		input_to_output()
		path_finder()
		
	Parser Methods:
		read() --------> output
		access() ------> output and display
		write() -------> output and overwrite
	Current Modules:
		html
		sql
		
	To Add:
		tkinter
		numpy
		matplotlib
		obd
		excel
		pdf
	
"""
name = "Erik Kosberg"
path = 'C:\\Documents\Code\Python\Parser'
doc_type = ['txt', 'pdf', 'xlsx', 'html']
input = {'some_data' : 123}
output = {'some_other_data' : 456}

master_input_list = [name, path, doc_type, input, output]

#Parser gets called by main; however, can hold completely separate 																	 attributes and methods within it
class Parser():
	def __init__(self):
		#initialize key attributes here
		self.name = name
		self.path = path
		self.doc_type = doc_type
		self.input = input
		self.output = output
		self.files = ['read.txt', 'write.txt']
	#Basic Functions
	def input_to_output(input, output):
		"""
			this function will overrite the output to the input set, useful to include all data	in larger sets that might want to filter out later on. 
		"""
		n()
		print("Before:	" + str(input))
		input = output
		print("After:		" + str(input))
		
	def content_handler(Content):
		"""
	
		This right here is where we can actually establish our own link
		to the content in order to connect the data for Penguin.py,
		access.py, and Content.py
		
		Content is the name of the module and it has one main function
		that we can use to read in data:	 content_import()
		
		Access the content using .content on an imported object."""
		#content = {"data1": 2, "data2": 2, "data3": 3} #store data here
		content = Content.content_import.content()
		
		#Add new data to the write file here
		#content["data4"] = 4

		#Re-initialize the list
		content = [p + ":	"+ str(value) +"\n" for p, value in content.items()]
		
		return content
		
	def data_overview(content):
		print("Previous Write :")
		print(content)
		n()

		print("CURRENT DATA")
		#Parse the data
		parse_key = ":\t"
		for x in content:
			x.split(parse_key)
			x = x[:-1]
			print(x)
		n()
		
	def path_finder(path):
		"""
			return the relevant file paths and check whether or not the are both formatted and valid
		"""
	def file_reader(file):
		"""
			Open a file and read in all lines, print and close when finished.
			
		"""
		mode = 'r'
		print("Reading Filename:		" + str(file))
		reader = open(file, mode)
		lines = reader.readlines()
		print("Total Lines Found:	" + str(len(lines)))
		reader.close()
		return lines
	def file_writer(file, lines, content, mode):
		"""
			Open and write a list of lines; 
				include mode in case you want to append/create new file
				without having to create whole new function.
			
			file: the txt file you are writing to
			lines: passed to print at the end
			content: the list you are writing to the file
			mode: 'r' for read, 'w' for write(overwrite)
						'x' for new,  'a' for append
		"""
		print("Writing Filename:		" + str(file))
		reader = open(file, mode)
		reader.writelines(content)
		new_lines = str(len(content))
		print(lines)
		
	def line_searcher(key, lines):
		"""
		Loop through lines to search for key words:
				based on the key of your choosing, you can
				loop through lines(as a list) using this function to
				very quickly find the index your text.
				
		If we know what line(s) the text is on, we can
		quickly narrow down our search. 
		"""
		n()
		print("Key Name:	" + str(key))
		n()
		
		set_search = lambda x: [z for z, value in lines.items()]
		search = lambda x: [z for z in (lines) if x in z]
		found = lines.index(search(key)[0])
		
		all_possibilities = search(key)
		all_set = {}
		
		for x in all_possibilities:
			all_set[search(x)[0]] = x 
			
		print("Found your key the first time on line: " + str(found))
		print("All the times found:	" + str(all_possibilities))
		
	#Parser Methods
	#not currently in use - see readP
	def read(path):
		"""
			read all lines in a file with the input stored in a list
			
		"""
		lines = [split for split in range(10) if split % 2 == 0]
		file = [line for line in lines]
		print("Master List:	"	+ str(file))
	#main read function
	def readP(files):
	#Read the read file in to 'lines1'; stored as list
		lines1 = Parser.file_reader(files[0])
		print(lines1)
		n()
		#Read the write file in to 'lines2' stored as list
		lines2 = Parser.file_reader(files[1])
		print(lines2)
		n()
		lines = lines2
		return lines
	def writeP(files,lines,content):
		files = ['read.txt', 'write.txt']
		#Overwrite the write file with live data
		mode = 'w'
		Parser.file_writer(files[1], lines, content, mode)

	def write():
		"""
			makes a call to input_to_output(), allowing us to use separate modifiers in each
			
		"""
		Parser.input_to_output(input, output)
		
	#Additional Modules
	class html():
		print("you found the html file")
		n()
	class sql():
		print("you found the sql table")
		n()
	
class Plot():
	"""
	Generic Plotting Class to Analyze Data:
		accepted as x and y inputs in the list data type
	"""

	import numpy as np
	import matplotlib.pyplot as plt
	
	plt.title('Chart')
	plt.ylabel('erik')
	plt.xlabel('kosberg')
	
	def __init__(self):
			print("plot stuff")
			plt.show()
		
class main():
	def __init__(self):
		name = "Erik" #only exists in main
		Parser() #this makes a call to Parser __init__

#if __name__ == '__main__':
main()
	
#connect using Parser.read()
#Parser.read(path)
#once the connection has been established, overwrite files using the following command:
#Parser.write()
#Parse html using the html subclass
#Parser.html()
#Parse sql using the sql subclass
#Parser.sql()

#Parser.line_searcher(key, lines2)

"""

#Part 2 - Defining Modules

	Now that we got our blueprints laid out for how our data is being broken up, we can
	start to define some modules or tools that allow us to manipulate and read in that data
	using our blueprints as a framework.
	
"""

"""""""""""""""""""""
*								    *
*	  Erik Kosberg    *
*								    *
"""""""""""""""""""""
