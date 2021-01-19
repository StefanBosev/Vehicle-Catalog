from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from database import DB

from user import User
from vehicle import Vehicle

app = Flask(__name__)

auth = HTTPBasicAuth()

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        values = (
            None,
            request.form['username'],
            User.hash_password(request.form['password'])
        )
        User(*values).create()

        return redirect('/')

@app.route('/login')
def login_button():
    return render_template('login.html')

@app.route('/services')
def services_button():
    return render_template('services.html')

@app.route('/view_my_vehicles')
@auth.login_required
def view_vehicles():
    with DB() as db:
        owner_id = db.execute('''
            SELECT user_id FROM Users WHERE username = ?
            ''', auth.username).fetchone()
        return render_template('view_vehicles.html', vehicle = Vehicle.find_by_owner(owner_id))

@app.route('/view_my_vehicles/<int:vehicle_id>')
@auth.login_required
def show_vehicle(vehicle_id):
    vehicle = Vehicle.find_by_id(vehicle_id)
    return render_template('view_vehicles.html', vehicle = vehicle)

@app.route('/view_my_vehicles/<int:vehicle_id>/edit', methods=['GET', 'POST'])
@auth.login_required
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
@auth.login_required
def add_vehicle():
    if request.method == 'GET':
        return render_template('new_vehicle.html')
    elif request.method == 'POST':
        #owner_id should be gotten from login?
        values = (None, request.form['owner_id'], request.form['model'], request.form['colour'], request.form['manufacture_year'])
        Vehicle(*values).create()
        return redirect(url_for('view_vehicles'))

@app.route('/view_my_vehicles/<int:vehicle_id>/delete', methods=['POST'])
@auth.login_required
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.find_by_id(vehicle_id)
    vehicle.delete()

    return redirect(url_for('view_vehicles'))

if __name__ == '__main__':
    app.run()