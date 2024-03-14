<h2>DoomBox</h2>
An automated insecure web server, initially developed for a packet sniffing and traffic analysis demo in my Cyber Clinic workshops. Now evolved into an OWASP inspired testing environment for your localhost!


Common vulnerabiltiies added for testing. Currently supporting:
  - [A3:2017-Sensitive Data Exposure (HTTP Logins)](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure "A3:2017-Sensitive Data Exposure (HTTP Logins)")
  - [A2:2017-Broken Authentication (Login Page Bruteforcing)](https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication "A2:2017-Broken Authentication (Login Page Bruteforcing)")
  - [A7:2017-Cross-Site Scripting (Reflective XSS)](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS))
  - [A1:2017-Injection (Remote Code Execution)](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection "A1:2017-Injection (Remote Code Execution)")

<h2>Lite vs Docker</h2>

<b>Lite:</b>
  
  - Simplicity in mind 
  - Purely Python based
  - Web Server hosted on users local file system
  - HTTP & PHP Servers - Ports 8000 (HTTP) & 8001 (PHP)

<b>Docker:</b>

  - Initialised through a Python script for ease of access!
  - Hugely greater scalability for vulnerabilities
  - Dedicated Apache Web Server (Reverse Shells are reliable & accurate)
  - Ran over a 172.16.0.0/16 subnet on port 8080

<br> 

`git clone https://github.com/Stuub/DoomBox`

<h2>Spin up in seconds!</h2>

![image](https://github.com/Stuub/PacketSniffing/assets/60468836/c1ac15bb-a5c6-4477-8306-ea1aebe2675a)

<h2>Login Portal</h2>

![image](https://github.com/Stuub/PacketSniffing/assets/60468836/0410cbce-acf8-4e2a-8c11-fbf070917c2c)

<h2>XSS</h2>

![image](https://github.com/Stuub/PacketSniffing/assets/60468836/af9fd9bc-79c6-4f3b-9028-dddee3e4a34c)

<h2>RCE</h2>

![whatTheShell](https://github.com/Stuub/PacketSniffing/assets/60468836/6ac42568-61cc-4fa1-ab21-fba177437858)
