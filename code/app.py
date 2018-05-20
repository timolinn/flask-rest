from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item} 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': f'Item with name {name} already exists'}, 400


        new_item = {
            'name': name,
            'price': 0.00
        }

        items.append(new_item)
        return new_item, 201

    def update(self, name):
        data = request.get_json()
        for item in items:
            if item['item'] == name:
                return {'update': data }
        new_item = {
            'name': name,
            'price': 0.00
        }

        items.append(new_item)
        return new_item


    def delete(self, name):
        pass

    def index(self):
        return items


class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')

app.run(debug=True)