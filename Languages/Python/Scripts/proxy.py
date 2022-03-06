import SimpleWebSocketServer
import SimpleHTTPSServer
import urllib
PORT = 9012
"""

	A proxy sits between the client and server.

	It receives requests from the client, sends them to server,
	receives response from server, and sends response to client.

	Used for hiding the server's ip, performance, and security.

"""
class Proxy(SimpleHTTPSServer.SimpleWebSocketServer):
   def do_GET(self):
      url=self.path[1:]
      self.send_response(200)
      self.end_headers()
      self.copyfile(urllib.urlopen(url), self.wfile)
httpd = SimpleWebSocketServer.SimpleWebSocketServer('localhost', PORT, Proxy)
print ("Proxy Srever at" , str(PORT))
httpd.serveforever()
