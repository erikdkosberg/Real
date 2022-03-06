import os
pi = input("Which pi would you like to connect to? ('s' for Server; 'r' for Robot')")

pi_map = {
	'r': '192.168.86.47',
	's': '192.168.86.48'
}

os.system("ssh pi@%s" % pi_map[pi])
