"""
	This script allows backend access to the text files, which we will
	be using to store and manipulate our data
	
	We will be using the read file to store data to the write file 
	to read in from in live time(indicating the most recent data)

"""
from Penguin import *
import Content

#connect our content
con = Parser.content_handler(Content)

key = 'data' #use this to search through lists with line_searcher()

#Access Key Attributes and Methods here:
files = ['read.txt', 'write.txt']

Parser.data_overview(con)
lines = Parser.readP(files)
Parser.writeP(files, lines, con)

#Create new file, if none already exists
mode = 'x'

#Access the write file directly
#writelines = Parser.file_reader(files[1])
#print("Verify Data:")
#print(writelines)

#lookup the index of certain key values in the list
Parser.line_searcher(key, lines)
