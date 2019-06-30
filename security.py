from models.user import UserModel

# OLD WAY TO CREATE A USER AND MAP IT WITH ID AND USERNAME
# users = [
#     User(1, 'bob', 'asdf')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # the client sends username and password
    # if everything is ok then the user is returned
    # and jwt creates an encoded token and sends it back to the client
    # the client receives the jwt token
    # and then the client sends back the jwt token in the authorization header to the server
    # the server decodes the token and calls the identity function
    # and verifies that the identity from the token exists in one of the users
    # the identity returns the user if it matches the id, in case the id does not match
    # it returns None and the server does not give permission to authorize the client
    # if it exists then the server responds positively to the client
    # and give him access to the resource he asked for

    # THIS METHOD SHOULD RETURN A WHOLE USER object, which will have id, username, password
    # OR it should return None
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    # THIS METHOD SHOULD RETURN A WHOLE USER object, which will have id, username, password
    # OR it should return None
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
