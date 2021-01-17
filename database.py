import mysql.connector

DB_NAME = 'vehicle_catalog'

connection = mysql.connector.connect(
  host="127.0.0.1",
  database= DB_NAME
)


connection.cursor().execute(
    '''CREATE TABLE Users 
    (
        user_id int primary key auto_increment,
        username varchar(20) unique not null,
        password varchar(50) not null
    )'''
)

connection.cursor().execute(
    '''CREATE TABLE Vehicles
    (
        vehicle_id int primary key auto_increment,
        owner_id int not null,
        model varchar(40) not null,
        colour varchar(20) not null,
        manufacture_year date not null,
        FOREIGN KEY(owner_id) REFERENCES Users(user_id)
    )'''
)

connection.cursor().execute(
    '''CREATE TABLE Services
    (
        service_id int primary key auto_increment,
        vehicle_id int not null,
        services enum('change oil', 'change tires', 'test breaks', 'change overlays', 'change belts', 'test transmission', 'change pads'),
        service_date date not null,
        FOREIGN KEY(vehicle_id) REFERENCES Vehicles(vehicle_id)
    )'''
)

connection.commit()

class DB:
    def __enter__(self):
        self.connection = mysql.connector.connect(
                            host="127.0.0.1",
                            database= DB_NAME
                        )
        return self.connection.cursor()

    def __exit__(self, type, value, traceback):
        self.connection.commit()