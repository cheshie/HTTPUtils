from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class S(BaseHTTPRequestHandler):
    def do_POST(self): 
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        logging.info(f"Path: {self.path}\n"
                     f"Headers:\n{self.headers}\n\n"
                     f"Body:\n{post_data.decode()}\n")
        self.send_response(200)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    httpd = HTTPServer(('', 80), S)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
