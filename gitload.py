import os

class gitref():
	"""Simple class to update the current repo"""

	def __init__(self):

		self.comment = str(input("Enter a comment for this commit\n"))

		os.system("git init")
		os.system("git add .")
		os.system("git commit . -m '%s'" % (self.comment))
		os.system("git push -u -f origin master")
		os.system("clear")
		
gitref()
