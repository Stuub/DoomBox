<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve username and password from the form
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Check if username and password are correct (for demonstration purposes, hardcoded credentials are used)
    $valid_username = "user123";
    $valid_password = "password123";

    if ($username === $valid_username && $password === $valid_password) {
        // Authentication successful
        echo "Login successful!";
    } else {
        // Authentication failed
        echo "Invalid username or password.";
    }
}
?>
