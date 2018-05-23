import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def querydb(cls, sql, *args):
        cursor = UserModel.open_connection(cls)
        res = cursor.execute(sql, (*args,))
        results = res.fetchall()

        UserModel.close_connection(cls)

        return results

    def open_connection(self):
        self.connection = sqlite3.connect('data.db')
        return self.connection.cursor()

    def close_connection(self):
        self.connection.close()