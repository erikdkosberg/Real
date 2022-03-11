import os

class Server:
    """"
    PHP localhost interface with argument parsing
    done at the command line.

    Our 'Server' will host three main files:
        1.) index.html
        2.) script.js
        3.) style.css
    
    """

    # Go to the server directory
    def __init__(self):
        os.chdir("Server/")


    # Start via system calls to php on the localhost
    def start_server(self):
        os.system("php -S localhost:8000")
        os.system("clear") # php will pause execution
        return "SERVER DOWN..." 


    # Parse out any arguments to modify server configuration
    def main(self):
        # TODO - arg parsing before server starts
        return self.start_server()


print(Server().main())