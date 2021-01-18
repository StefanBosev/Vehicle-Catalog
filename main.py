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

@app.route('/view_my_vehicles_button')
def view_vehicles():
    #owner_id from login
    return render_template('view_vehicles.html', vehicle = Vehicle.find_by_owner())

@app.route('/view_my_vehicles/<int:vehicle_id>')
def show_vehicle(vehicle_id):
    vehicle = Vehicle.find_by_id(vehicle_id)
    return render_template('view_vehicles.html', vehicle = vehicle)

@app.route('/view_my_vehicles/<int:vehicle_id>/edit', methods=['GET', 'POST'])
def edit_vehicle(vehicle_id):
    vehicle = Vehicle.find_by_id(vehicle_id)
    if request.method == 'GET':
        return render_template('edit_vehicle.html', vehicle = vehicle)
    elif request.method == 'POST':
        vehicle.model = request.form['model']
        vehicle.colour = request.form['colour']
        vehicle.manufacture_year = request.form['manufacture_year']
        vehicle.save()

        return redirect(url_for('show_vehicles', vehicle_id=vehicle.vehicle_id))

@app.route('/view_vehicles/new', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'GET':
        return render_template('new_vehicle.html')
    elif request.method == 'POST':
        #owner_id should be gotten from login?
        values = (None, request.form['owner_id'], request.form['model'], request.form['colour'], request.form['manufacture_year'])
        Vehicle(*values).create()
        return redirect(url_for('view_vehicles'))

@app.route('/view_my_vehicles/<int:vehicle_id>/delete', methods=['POST'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.find_by_id(vehicle_id)
    vehicle.delete()

    return redirect(url_for('view_vehicles'))

if __name__ == '__main__':
    app.run()