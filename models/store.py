from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # with the command below
    # we can get the items that belong to each store
    # for example
    # Store(id=1, name="pharaoh").items -> will give us the items that belong to pharaoh
    # and the link of the items is done with the foreign key in the items model
    # when an item is created, the line below creates an object for that item in order to create
    # a relationship between the item and the store
    # for example when item with id=1 and store_id=1 is created, then the SotreModel creates
    # an object to indicate the relationship between the item and the corresponding store_id
    # with lazy='dynamic', we skip the automatic creation of the object that indicates the store_id
    items = db.relationship('ItemModel', lazy='dynamic')
    # when we run the command above, an object StoreModel is created for each item
    # if we have a lot of items, this will take a lot of time and therefore
    # we use lazy=dynamic, and the object is created only when we want to load it with the command ".all"



    #price = db.Column(db.Float(precision=2))

    def __init__(self, name):
        self.name = name

    def json(self):

        return {"name": self.name, "items": [item.json() for item in self.items.all()]}
        #return {"name": self.name, 'price': self.price}

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


