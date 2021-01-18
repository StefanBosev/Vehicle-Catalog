from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth

from user import User
from vehicle import Vehicle

app = Flask(__name__)

# auth = HTTPBasicAuth()

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

@app.route('/login_button')
def login_button():
    return render_template('homepage.html')

@app.route('/home_button')
def home_button():
    return render_template('homepage.html')

@app.route('/services_button')
def services_button():
    return render_template('services.html')

@app.route('/view_my_cars_button')
def view_cars():
    return render_template('view_vehicles.html', vehicle = Vehicle.find_by_owner())

@app.route('/view_my_cars_button/<int:vehicle_id>')
def show_vehicle(vehicle_id):
    vehicle = Vehicle.find_by_id(vehicle_id)
    return render_template('view_vehicles.html', vehicle = vehicle)

if __name__ == '__main__':
    app.run()