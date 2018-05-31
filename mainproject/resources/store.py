from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200

        return {'store': 'store with name "{}" not found'.format(name)}, 404




    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'store with name {} already exists'.format(name)}, 400

        new_store = StoreModel(name)

        try:
            new_store.save_to_db()
        except:
            return {"message": "an error occured saving the store"}, 500

        return new_store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'store Deleted'}

    def put(self, name):
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "an error occured updating the store"}, 500

        return store.json()


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        # return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
