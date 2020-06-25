# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:58:13 2020

@author: Hossein
"""
from flask import Flask
from flask_restful import Resource, Api
from Classes.User.users import *
from Classes.Companies.Company import *
from Classes.Jobs.Jobs import *
from flask import jsonify


app = Flask(__name__)
api = Api(app)

#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}

api.add_resource(User, '/user')
api.add_resource(logIn, '/login')
api.add_resource(update_user,'/update_user')
api.add_resource(Company, '/company')
api.add_resource(update_company, '/update_company')
api.add_resource(Jobs,'/job')

if __name__ == '__main__':
    app.run(debug=True)







