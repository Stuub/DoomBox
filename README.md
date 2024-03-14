<h2>PacketSniffing</h2>
An automated insecure web server, initially developed for a packet sniffing and traffic analysis demo in my Cyber Clinic workshops. Now evolved into an OWASP inspired testing environment for your localhost!


Common vulnerabiltiies added for testing. Currently supporting:
  - [A3:2017-Sensitive Data Exposure (HTTP Logins)](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure "A3:2017-Sensitive Data Exposure (HTTP Logins)")
  - [A2:2017-Broken Authentication (Login Page Bruteforcing)](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication "A2:2017-Broken Authentication (Login Page Bruteforcing)")
  - [A7:2017-Cross-Site Scripting (Reflective XSS)](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)
  - [A1:2017-Injection (Remote Code Execution)](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection "A1:2017-Injection (Remote Code Execution)")

Utilising HTTP & PHP, initialises a server for each on ports 8000 (HTTP) & 8001 (PHP)

<h2>To use:</h2>
- Navigate to directory 'PacketSniffing'
- python3 server.py

Then go to browser and visit
http://localhost:8000/index.html

From here you can use the page as if it were any other website! Enjoy :)
