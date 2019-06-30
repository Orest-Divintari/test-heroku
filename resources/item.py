from flask import Flask, jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This should not be left blank'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item needs a store id'
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {"message": "item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"An item with name {name} already exists"}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data) # same with below
        #item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "an error occurred inserting the item"}, 500

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
            # item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "item was deleted successfully"}
        else:
            return {"message": "item does not exist"}


        # OLD CODE, WITHOUT SQLALCHEMY
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # if ItemModel.find_by_name(name):
        #     query = """DELETE FROM items WHERE name=?"""
        #     cursor.execute(query, (name,))
        #     connection.commit()
        #     connection.close()
        #     return {"message": "the item was deleted"}, 201
        # else:
        #     return {"message": "the item does not exist "}, 400


class Items(Resource):

    def get(self):
        items = [item.json() for item in ItemModel.query.all()]
        # items = list(map(lambda x: x.json(), ItemModel.query.all()))
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = """SELECT * FROM items"""
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})
        # connection.close()
        return {"items": items}

