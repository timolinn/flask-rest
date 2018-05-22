from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

import os

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = os.urandom(16)
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field is required"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': f'Item with name {name} already exists'}, 400

        data = Item.parser.parse_args()
        new_item = {
            'name': name,
            'price': data['price']
        }

        items.append(new_item)
        return new_item, 201

    def update(self, name):
        data = Item.parser.parse_args()
        for item in items:
            if item['name'] == name:
                item.update(data)
                return item
        new_item = {
            'name': name,
            'price': data['price']
        }

        items.append(new_item)
        return new_item


    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item Deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field is required"
        )
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(data)
        else:
            item.update(data)
        return item

    def index(self):
        return items


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')

app.run(debug=True)