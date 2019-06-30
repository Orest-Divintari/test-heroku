import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'uric'
api = Api(app)
jwt = JWT(app, authenticate, identity)

# creates the tables that we need
# according to the schema we gave to the Models file
# @app.before_first_request
# def create_tables():
#     db.create_all()


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')


@app.route('/')
def welcome():
    return 'welcome re arxidi'


if __name__ == 'main':
    from db import db
    db.init_app(app)
    app.run(debug=True)



