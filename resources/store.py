from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        else:
            return {"message": "this store does not exist"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": f"this store with name {name} already exists"}
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {"message": "An error occurred while creating the store"}, 500

            return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "the store was deleted"}
        else:
            return {"message": "store does not exist"}




class StoreList(Resource):

    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
