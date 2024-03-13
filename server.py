import http.server
import socketserver
import subprocess
import os
import sys
import signal

# Set the ports for the Python and PHP servers
PYTHON_PORT = 8000
PHP_PORT = 8001

# Define the request handler class for Python HTTP server
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the do_GET method to handle GET requests
    def do_GET(self):
        # Set the response status code
        self.send_response(200)
        # Set the content type header
        self.send_header('Content-type', 'text/html')
        # End the headers
        self.end_headers()
        # Read the HTML file and send it as the response
        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())

# Define the function to start the PHP server
def start_php_server():
    php_server_process = subprocess.Popen(["php", "-S", f"localhost:{PHP_PORT}", "-t", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return php_server_process

# Create a socket server for the Python HTTP server
with socketserver.TCPServer(("", PYTHON_PORT), MyHttpRequestHandler) as httpd:
    print(f"Python HTTP server running at localhost:{PYTHON_PORT}")

    # Start the PHP server
    php_server_process = start_php_server()
    print(f"PHP server running at localhost:{PHP_PORT}")

    try:
        # Start the Python HTTP server and keep it running until interrupted
        httpd.serve_forever()
    except KeyboardInterrupt:
        # If interrupted, terminate both servers
        print("\nShutting down servers...")
        httpd.shutdown()
        php_server_process.terminate()
        php_server_process.wait()
        print("Servers shutdown successfully.")