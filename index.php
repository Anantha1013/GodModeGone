<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Defeating the Olympus</title>
    <link rel="stylesheet" href="style.css">
    <?php
        $conn=new mysqli('localhost','root','','vulnerable-db')

        if($conn->connect_error){
            die("Connection failed: ". $conn->connect_error);
        }

        if(isset($POST['username']) && isset($_POST['password'])){
            $username=$_POST['username'];
            $password=$_POST['password'];

            $query="SELECT * FROM users WHERE username='$username' AND password='$password'";
            $result=$conn->query($query);

            if($result->num_rows >0){
                header("Location: flag1.html");  // Or use "page1.php" if dynamic
                exit();
            }else{
                echo "<script>
        alert('Invalid username or password. Please try again.');
        window.location.href = 'index.html'; // Redirect back to the login page
        </script>";
            }
        }
    ?>
</head>
<body>
    <div class="container">
        <header>
            <h1>GodModeGone!</h1>
            <p>Can you defeat the gods of Olympus?</p>
        </header>

        <section class="login-section">
            <h2>Get past the main gate first</h2>
            <form method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Your username"><br>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Your password"><br>

                <input type="submit" value="Enter Olympus">
            </form>
            <p>Hint: You can never get in straight up.Find any loophole to get in</p>
        </section>

        <footer>
            <p>Challenge the Gods. Defeat Olympus.</p>
            <p>&copy; 2024 Olympus Security Labs</p>
        </footer>
    </div>
</body>
</html>
