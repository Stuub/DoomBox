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
        echo "Login successful!";
        echo "Your username is: " . $username;
        echo "Your password is: " . $password;
    } else {
        // Authentication failed
        echo "Sorry ". $username . " Invalid username or password.";
    }
}
?>
