from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    # new column after we created the StoreModel
    # stores.id is the id column of the StoreModel
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('StoreModel')


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # Searches the database for the item with the given name
        # converts that item to an ItemModel object
        # returns only the first occurrence of that name
        return cls.query.filter_by(name=name).first()

        # The code below is without SQLAlchemy
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = """SELECT * FROM items WHERE name=?"""
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row)
    def save_to_db(self):
        # The insert is called by an ItemModel object
        # therefore we can say directly to store that object in the db
        # this method inserts an item if the item does not exist in the db
        # if it exists, it updates the item that is already in db
        db.session.add(self)  # store object in db
        db.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = """INSERT INTO items VALUES (?, ?)"""
        # cursor.execute(query, (self.name, self.price))
        # connection.commit()
        # connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


