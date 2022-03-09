import os
os.chdir("Server/")

# Previous method - SimpleHttpServer in Python
# os.system("python3 -m http.server 8000")

# New method - using php
os.system("php -S localhost:8000")
