from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if login.method == 'GET':
        return render_template('login.html')
    elif login.method == 'POST':
        return redirect('/homepage.html')

@app.route('/login_button')
def login_button():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run()