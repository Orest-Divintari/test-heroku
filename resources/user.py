import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='You have to give a username'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='You have to give a username'
                        )

    def post(self):

        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "user already exists"}
        else:
            #user = UserModel(data['username'], data['password'])
            # with ** we say take the value of the first key as the first argument
            # and take the value of the second key as the second argument
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "user created successfully"}

        #
        # if UserModel.find_by_username(data['username']):
        #     return {"message": "this username already exists"}
        # else:
        #     connection = sqlite3.connect('data.db')
        #     cursor = connection.cursor()
        #     query = """INSERT INTO users VALUES (NULL, ?, ?)"""
        #     cursor.execute(query, (data['username'], data['password']))
        #     connection.commit()
        #     connection.close()
        #
        # return {"message": "user created successfully"}, 201





