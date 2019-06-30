import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# table = """CREATE TABLE users (id int,
#                             username text,
#                             password text)
#                             """
# cursor.execute(table)

user1 = {'id':1, 'username': 'uric', 'password': 'asdf'}
users = [
    {'id': 1, 'username': 'uric', 'password': 'asdf'},
    {'id': 2, 'username': 'orestis', 'password': 'qqqq'}
]
insert_query = "INSERT INTO users VALUES (:id, :username, :password)"
cursor.executemany(insert_query, users)

select_users = """SELECT * FROM users"""
cursor.execute(select_users)
print(cursor.fetchall())
connection.commit()
connection.close()