Automated setup for an insecure login page, for a packet sniffing and traffic analysis demo in my Cyber Clinic workshops!

Common vulnerabiltiies added for testing. Currently supporting:
  - A3:2017-Sensitive Data Exposure (HTTP Logins)
  - A7:2017-Cross-Site Scripting (Reflective XSS)

Using HTTP & PHP, initialises a server for each on ports 8000 (HTTP) & 8001 (PHP)

To use:
- Navigate to directory - 'PacketSniffing'
- python3 server.py

Then go to browser and type
http://localhost:8000/index.html

From here you can use the page as if it were any other website! Enjoy :)
