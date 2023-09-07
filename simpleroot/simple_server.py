import http.server
import socketserver

PORT = 9990

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.txt'     : 'text/plain; charset=utf-8',
                               '.json'    : 'application/json', 
                               '.xml'     : 'text/xml; charset=utf-8'} )

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()