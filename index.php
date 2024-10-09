<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Defeating the Olympus</title>
    <link rel="stylesheet" href="style.css">
    <script>
        function login(){
            var us=document.getElementById('username').value;
            var pass=document.getElementById('password').value;

            if(us=='dionysus'  && pass=='whiskey'){
                window.location.href='page1.html';
            }else{
                alert("Incorrect  credentials , Maybe you'll never find using brute force. Try another way");
            }
        }
    </script>
</head>
<body>
    <div class="container">
        <header>
            <h1>GodModeGone!</h1>
            <p>Can you defeat the gods of Olympus?</p>
        </header>

        <section class="login-section">
            <h2>Get past the main gate first</h2>
            <form onsubmit="event.preventDefault(); login();">
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
