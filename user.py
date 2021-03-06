import hashlib

from database import DB
from vehicle import Vehicle

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def create(self):
        with DB() as db:
            values = (self.username, self.password)
            db.execute('''
                INSERT INTO Users(username, password) VALUES(?, ?)
                ''', values)

            return self

    def delete(self):
        with DB() as db:
            db.execute('''
                DELETE FROM Users WHERE user_id = ?
                ''', self.id)

    @staticmethod
    def find_by_id(user_id):
        with DB() as db:
            db.execute('''
            SELECT * FROM Users WHERE user_id = ?
            ''', user_id)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_password(self, new_password):
        return self.password == hashlib.sha256(new_password.encode('utf-8')).hexdigest()