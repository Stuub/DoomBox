<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            width: 300px;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
    <title>Authenticated?</title>
</head>
<body>
    <?php
        // Check if form is submitted
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Retrieve username and password from the form
            $username = $_POST["username"];
            $password = $_POST["password"];

            // Check if username and password are correct (for demonstration purposes, hardcoded credentials are used)
            $valid_username = "username";
            $valid_password = "password";

            if ($username === $valid_username && $password === $valid_password) {
                // Authentication successful
                echo "<div class='container'><h2>Login successful!</h2>";
                echo "<p>Welcome back " . $username . "</p>";
                echo "<p>Click here to go to the <a href='http://".$_SERVER['HTTP_HOST']."/rce.php'>RCE page</a>.</p></div>";
            } else {
                // Authentication failed
                echo "<div class='container'><h2>Sorry ". $username . ", Invalid username or password.</h2></div>";
            }
        }?>
</body>
</html>

