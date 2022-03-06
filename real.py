
import os

os.chdir("Server/HTML/Websites/local/")
os.system("python3 -m http.server 8000")
webbrowser.open("http://localhost:8000")

