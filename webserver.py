# Load the website on local with Python WEBSERVER
from http import server, HTTPStatus
import sys

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Error: Missing argument...\nUsage: python webserver.py [PORT NUMBER]\n")
    else:
        handler = server.SimpleHTTPRequestHandler
        adresse = 'localhost'
        try:
            port = int(sys.argv[1]) # Turn the port given as input into Integer
        except:
            print("Error: Port number invalid...\n")
        else:
            print("Serving on address: http://localhost:%d/" %(port,))
            serveur = server.HTTPServer((adresse,port), handler)
            serveur.serve_forever()
            