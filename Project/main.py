"""
    This main.py file is the main file for this project.
    The server starts from here. All the endpoints are registered in this file.
    This file helps in routing the incoming required api request to the appropriate resource.
    This file has all the main imports required to create the server.
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from security import authenticate, identity
from employees import Employee, employeeList

app = Flask(__name__)
app.secret_key = 'shriya'
api = Api(app)

jwt = JWT(app, authenticate, identity)   # This will generate a token

# Employee and EmployeeList class are shifted to items.py file and the required imports are added to this file
api.add_resource(Employee, '/employee')     #http://127.0.0.1:5000/employee
api.add_resource(employeeList, '/employees')
api.add_resource(UserRegister, '/register')
# print('This is from main.py: ', __name__)

if __name__ == '__main__':   # If the main.py file is executed then only the server starts running
    app.run(port=5000, debug=True)