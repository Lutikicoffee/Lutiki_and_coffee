import os
from flask import Flask, request

app = Flask(__name__)

# Чтение логина и пароля из системных переменных, так секьюрнее
admin_username = os.getenv('ADMIN_USERNAME')
admin_password = os.getenv('ADMIN_PASSWORD')

@app.route('/secret-super-secure-login', methods=['POST'])
def admin():
    username = request.form['username']
    password = request.form['password']
    
    if username == admin_username and password == admin_password:
        return "Welcome to Admin Panel!"
    else:
        return "Unauthorized", 401

if __name__ == "__main__":
    app.run()