from flask import Flask, request, redirect

app = Flask(__name__)

admin_credentials = {'username': 'admin', 'password': '7774m4supp3r4dmin777'}

@app.route('/secret-super-secure-login', methods=['POST'])
def admin():
    username = request.form['username']
    password = request.form['password']
    if username == admin_credentials['username'] and password == admin_credentials['password']:
        return "Welcome to Admin Panel!"
    else:
        return "Unauthorized", 401