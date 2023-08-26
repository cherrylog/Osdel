from colorama import Fore, Back, Style
print(Fore.WHITE + "\n")
from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ("localhost", 8080)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()
