"""
    This main.py file is the main file for this project.
    The server starts from here. All the endpoints are registered in this file.
    This file helps in routing the incoming required api request to the appropriate resource.
    This file has all the main imports required to create the server.
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from resources.user import UserRegister
from security import authenticate, identity
from resources.items import Item, ItemList

app = Flask(__name__)
app.secret_key = 'shriya'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# Item and ItemList class are shifted to items.py file and the required imports are added to this file
api.add_resource(Item, '/item')     #http://127.0.0.1:5000/item
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
# print('This is from main.py: ', __name__)

if __name__ == '__main__':
    app.run(port=5000, debug=True)