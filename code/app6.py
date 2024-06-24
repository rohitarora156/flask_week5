from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from user import UserRegister
from item import Item,ItemList

app = Flask(__name__)
app.secret_key = 'Rohit'
api = Api(app)

jwt = JWT(app,authenticate,identity) #this creates a new endpoint : /auth

    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':             #this is done to check whether the file is running the same fikle of itself or other 
    app.run(port = 2000,debug = True)
