import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # cls = UserModel which inherits from db.Model, which is the SQLAlchemy
        # therefore it inherits the methods query.filter_by
        # and that's why we do cls.query.filter_by
        # the SQLAlchemy returns always an object from the DATABASE
        # and the first() method gives us only the first object with the given username
        return cls.query.filter_by(username=username).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(row[0], row[1], row[2])
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    def save_to_db(self):
        # using the db object ( which is the SQLAlchemy) from the db.py
        # the db object has a session.add method which takes as argument an object
        # and the object is stored in the database
        # so when this method is called, is called by an object and therefore the object itself is stored in the db
        # for example we create an object UserModel
        # user = UserModel(1, 'uric', 'orestis')
        # user.save_to_db()
        # so the item user passing itself to "save_to_db" and "save_to_db" stores the object user in the database
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM users WHERE id=?"
        # cursor.execute(query, (_id,))
        # row = cursor.fetchone()
        # if row:
        #     user = UserModel(row[0], row[1], row[2])
        # else:
        #     user = None
        # connection.close()
        # return user
