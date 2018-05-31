import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from dbman import DBMan
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field is required"
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item require a store id"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200

        return {'item': 'Item with name "{}" not found'.format(name)}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'Item with name {} already exists'.format(name)}, 400

        data = Item.parser.parse_args()
        new_item = ItemModel(name, **data)

        try:
            new_item.save_to_db()
        except:
            return {"message": "an error occured saving the item"}

        return new_item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item Deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        try:
            item.save_to_db()
        except:
            return {"message": "an error occured updating the item"}

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
