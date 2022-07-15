import sqlite3

class UserModule:
    ''' 
        This class will verify the incoming (through request) user credentials, username and password. 
    '''
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findUsername(cls, username):
        '''
            This function will identify the user whether that user present in the database, based on his username.
        '''
        print("This is Username from findUsername: ", username)
        connection = sqlite3.connect('data.db')     # This will create a connection to the database.
        cursor = connection.cursor()                # This will create a cursor object of the existing connection.

        query = "SELECT * FROM users WHERE username = ?"    # This
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        print("This is the row variable: ", row)
        if row:
            user = cls(*row)
            print("This is the user from database: ", user)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def findId(cls, _id):
        '''
            This function will identify the user whether that user present in the database, based on his username.
        '''
        print(_id)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        print("This is from findId: ", row)
        print("This is from findId, row type: ", type(row))
        if row:
            user = cls(*row)
            print("This is the user from database: ", user)
        else:
            user = None

        connection.close()
        return user