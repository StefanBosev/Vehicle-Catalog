# enum('change oil', 'change tires', 'test breaks', 'change overlays', 'change belts', 'test transmission', 'change pads')

from database import DB

class Service:
    def __init__(self):
        self.services = ('change oil', 'change tires', 'test breaks', 'change overlays', 'change belts', 'test transmission', 'change pads')

    @staticmethod
    def change_oil(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'change oil')

    @staticmethod
    def change_tires(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'change tires')

    @staticmethod
    def test_breaks(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'test breaks')

    @staticmethod
    def change_overlays(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'change overlays')

    @staticmethod
    def change_belts(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'change belts')

    @staticmethod
    def test_transmission(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'test transmission')

    @staticmethod
    def change_pads(car_id):
        with DB() as db:
            db.execute('''
            INSERT INTO Services(vehicle_id, services) VALUES(?, ?)
            ''', car_id, 'change pads')