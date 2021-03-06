from database import DB

class Vehicle:
    def __init__(self, vehicle_id, owner_id, model, colour, manufacture_year):
        self.vehicle_id = vehicle_id
        self.owner_id = owner_id
        self.model = model
        self.colour = colour
        self.manufacture_year = manufacture_year
        with DB() as db:
            db.execute('''
            INSERT INTO Vehicles(owner_id, model, colour, manufacture_year) VALUES(?, ?, ?, ?)
            ''', owner_id, model, colour, manufacture_year)

    @staticmethod
    def get_all():
        with DB() as db:
            all_rows = db.execute('''SELECT * FROM Vehicles''').fetchall()
            return [Vehicle(*single_row) for single_row in all_rows]

    @staticmethod
    def get_all_for_owner(owner_id):
        with DB() as db:
            all_vehicles  = db.execute('''SELECT * FROM Vehicles WHERE owner_id = ?''', owner_id).fetchall()
            return [Vehicle(*vehicle) for vehicle in all_vehicles]

    @staticmethod
    def find_by_id(vehicle_id):
        with DB() as db:
            row = db.execute('''
                SELECT * FROM Vehicles WHERE vehicle_id = ?
                ''', vehicle_id)

            if row is None:
                return
            return Vehicle(*row)

    @staticmethod
    def find_by_owner(owner_id):
        with DB() as db:
            vehicles = db.execute('''
                SELECT * FROM Vehicles WHERE owner_id = ?
                ''', owner_id)

            if vehicles is None:
                return
            return [Vehicle(*vehicle) for vehicle in vehicles]

    def create(self):
        with DB() as db:
            values = (self.owner_id, self.model, self.colour, self.manufacture_year)
            db.execute('''
                INSERT INTO Vehicles(owner_id, model, colour, manufacture_year)
                ''', values)

            return self

    def save(self):
        with DB() as db:
            values = (self.model, self.colour, self.manufacture_year)
            db.execute('UPDATE posts SET model = ?, colour = ?, manufacture_year = ? WHERE vehicle_id = ?', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('''
                DELETE FROM Vehicles WHERE id = ?
                ''', self.vehicle_id)
