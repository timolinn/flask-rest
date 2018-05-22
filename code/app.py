from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

import os

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = os.urandom(16)
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')

app.run(debug=True)