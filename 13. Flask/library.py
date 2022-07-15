from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'shriya'
api = Api(app)

jwt = JWT(app, authenticate, identity)

books = []


class Book(Resource):
    # @jwt_required()
    def get(self):
        data = request.get_json()
        book = next(filter(lambda x: x['name'] == data['name'], books), None)
        return {'book': book}, 200 if book else 404
        

    def post(self):
        data = request.get_json()
        if next(filter(lambda x : x['name'] == data['name'], books), None):
            return {'message' : "A book with name '{}' already exists.".format(data['name'])}, 400
        else:
            book = {'name' : data['name'], 'author' : data['author'], ' no_of_pages' : data['no_of_pages'], 'type' : data['type'], 'used' : data['used'], 'discount' : data['discount'], 'charges' : data['charges'], 'address' : data['address'], 'price' : data['price'], 'returnable': data['returnable']}
            books.append(book)
            return books, 201

    def delete(self):
        global books
        data = request.get_json()
        books = list(filter(lambda x: x['name'] != data['name'], books))
        return {'message' : 'Book deleted!'}

    def put(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('price',
        #                     type = float,
        #                     required = True,
        #                     help = "This is required!"
        #                     )
        # parser.add_argument('name',
        #                     type = str,
        #                     required = True,
        #                     help = "This is required!"
        #                     )
        
        # data = parser.parse_args()
        # print(data)
        # print(dict(data))
        # print(type(data))

        data = request.get_json()
        book = next(filter(lambda x: x['name'] == data['name'], books))
        if book is None:
            book = {'name' : data['name'],  'author' : data['author'], ' no_of_pages' : data['no_of_pages'], 'type' : data['type'], 'used' : data['used'], 'discount' : data['discount'], 'charges' : data['charges'], 'address' : data['address'], 'price' : data['price'], 'returnable': data['returnable']}
            books.append(book)
        else:
            books.update(data)
        return book

        
class BookList(Resource):
    def get(self):
        return {'books' : books}


api.add_resource(Book, '/book')     #http://127.0.0.1:5000/student/Shriya
api.add_resource(BookList, '/books')


app.run(port=5000, debug=True)