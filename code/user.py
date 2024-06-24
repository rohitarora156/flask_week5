import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
        
    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,)) #comma to show its not a single value , its a tuple passing of parameter in ?
        row = result.fetchone()

        if row:
            user = cls(row[0],row[1],row[2]) #you can write User in place of cls and *row inplace of aLL the arguments
        else:
            user = None
        
        connection.close()
        return user


    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,)) #comma to show its not a single value , its a tuple passing of parameter in ?
        row = result.fetchone()

        if row:
            user = cls(row[0],row[1],row[2]) #you can write User in place of cls and *row inplace of aLL the arguments
        else:
            user = None
                
        connection.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',type = str, required = True, help = "This field cannot be blank")
    parser.add_argument('password',type = str, required = True, help = "This field cannot be blank")


    def post(self):

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"Message" : "A user with that username already exists"} , 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES(NULL,?,?)" #WHY NULL ? as auto increment of id is there
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"Message" : "User created Succesfully"} , 201
