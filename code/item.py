import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from dbman import DB

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field is required"
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item, 200
        return {'item': f'Item with name "{name}" not found'}, 404

    def find_by_name(self, name):
        sql = "SELECT * FROM items WHERE name=?"
        result = DB.select_one(sql, (name,))

        if result:
            return {'item': {'name': result[0], 'price': result[1]}}


    def post(self, name):
        if self.find_by_name(name)
            return {'message': f'Item with name {name} already exists'}, 400

        data = Item.parser.parse_args()
        new_item = {
            'name': name,
            'price': data['price']
        }

        sql = "INSERT INTO items VALUES(?,?)"
        DB.insert_one(sql, new_item['name'], new_item['price'])
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