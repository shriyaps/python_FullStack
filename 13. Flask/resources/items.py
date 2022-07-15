import sqlite3
from dbConfig import DatabaseConfig
from flask import Flask,request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from modules.items import ItemModule

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type = float,
        required = False,
        help = 'This is required field'
    )

    parser.add_argument(
        'name',
        type = str,
        required = True,
        help ='This is required field'
    )
    @jwt_required()
    def get(self):
        data = Item.parser.parse_args()
        item = ItemModule.findItem(data['name'])
        if item:
            return item
        return {'message' : 'Item not found!'}, 404

    @jwt_required()
    def post(self):
        data = Item.parser.parse_args()
        if ItemModule.findItem(data['name']):
            return {'message' : "An item with name '{}' already exists.".format(data['name'])}, 400
        item = {'name' : data['name'], 'price' : data['price']}
        
        try:
            ItemModule.insert(item)
        except:
            return {"message" : "An error occured while inserting item"}, 500
        return item, 201
        
    @jwt_required()
    def delete(self):
        connection, cursor = DatabaseConfig('data').createConnection()
        data = Item.parser.parse_args()
        if ItemModule.findItem(data['name']): 
            query = "DELETE FROM items WHERE name = ?"
            cursor.execute(query, (data['name'],))

            connection.commit()
            connection.close()
            return {'message' : 'Item deleted!'}
        return{'message' : 'Item does not exist!'}

    def put(self):
        data = Item.parser.parse_args()
        item = ItemModule.findItem(data['name'])
        updatedItem = {'name' : data['name'], 'price' : data['price']}

        if item is None:
            try:
                ItemModule.insert(updatedItem)
            except:
                return {"message" : "An error occured while inserting item"}, 500
        else:
            try:
                ItemModule.update(updatedItem)
            except:
                return {"message" : "An error occured while updating item"}, 500
        return updatedItem


class ItemList(Resource):
    def get(self):
        connection, cursor = DatabaseConfig('data').createConnection()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        

        items = []
        for row in result:
            items.append({'name' : row[0], 'price' : row[1]})
            connection.commit()
            connection.close()
        return {'items' : items}

        