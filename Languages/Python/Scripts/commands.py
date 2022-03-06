n = lambda : print('\n')

class Command():
	def usage():
		print("Welcome to ampy!")
		n()
		print("access commands in command prompt with following syntax:")
		print("		i.e. ampy tty0 -c --> connect to serial tty0")
		n()
		print("List of available commands:")
		print("	-c -connect : connects to the specified serial port ; ampy port command")
		print("	-r -read : reads a specified PID from connected port ; ampy command PID")
		print("	-ls -list : list all current standard sensor values ; ampy command")
		print("	-l -log : log a specified PID to a specified file ; ampy command PID path")
		print("	-z -reset : resets the device ; ampy command")
		print("	-sp	-serial : auto detects the serial settings ; ampy command")
		
	def main():
		Command.usage()
			
Command.main()
