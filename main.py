from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from user import User

app = Flask(__name__)

auth = HTTPBasicAuth()

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if register.method == 'GET':
        return render_template('register.html')
    elif register.method == 'POST':
        values = (
            None,
            request.form['username'],
            User.hash_password(request.form['password'])
        )
        User(*values).create()

        return redirect('/')

@app.route('/register_button')
def register_button():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run()