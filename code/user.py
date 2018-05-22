import sqlite3
from flask_restful import reqparse, Resource

class User():

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        query = "SELECT * FROM users WHERE username=?"
        row = cls.query(query, username)

        if row: return cls(*row[0])
        return None

    @classmethod
    def find_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id=?"
        row = cls.query(query, user_id)

        if row: return cls(*row[0])
        return None

    @classmethod
    def query(cls, sql, *args):
        cursor = User.open_connection(cls)
        res = cursor.execute(sql, (*args,))
        results = res.fetchall()

        User.close_connection(cls)

        return results

    def open_connection(self):
        self.connection = sqlite3.connect('data.db')
        return self.connection.cursor()

    def close_connection(self):
        self.connection.close()

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field is required"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field is required"
    )

    def post(self):
        data = self.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message': 'Username taken. Try another username'}, 400

        sql = "INSERT INTO users VALUES (NULL, ?, ?)"
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(sql, (data['username'], data['password']))

        conn.commit()
        conn.close()

        return {'message': 'User registered successfully'}, 201





# another = User.find_by_id(1)
# print(another.username)