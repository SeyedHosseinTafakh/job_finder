# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:24:20 2020

@author: Hossein
"""


import pandas as pd
import numpy as np
from flask_restful import Resource , reqparse
import werkzeug
from werkzeug.utils import secure_filename
from flask import jsonify ,request
from connector import *


def check_email_company(email):
    sql = ('select * from company where email = %s')
    val = (email,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if len(data)>0:
        return False
    return True




class Company(Resource):
    def get(self):
        sql = 'select * from user'
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',required=True)
        parser.add_argument('email',required=True)
        parser.add_argument('password',required=True)
        parser.add_argument('companyName',required=True)
        parser.add_argument('companyDescribtion',required=False)
        parser.add_argument('overview',required=False)
        parser.add_argument('links',required=False)
        parser.add_argument('Logo',required=False)
        args = parser.parse_args()
        if check_email_company:
            return jsonify("error : email already exist")
        sql = ('INSERT INTO company_profile (name , email , password , companyName ,companyDescribtion ,overview,links,Logo,api_key) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
        values =(
            args['name'],
            args['email'],
            args['password'],
            args['companyName'],
            args['companyDescribtion'],
            args['overview'],
            args['links'],
            args['Logo'],
            'api_key'
            )
        mycursor.execute(sql,values)
        mydb.commit()
        return jsonify(True)
    
    
    
class update_company(Resource):
    def post(self):
        def check_api_key(api_key):
            sql = ('select * from company where api_key = %s')
            val = (api_key,)
            mycursor.execute(sql,val)
            data = mycursor.fetchall()
            if len(data)<0:
                return False
            return data
        parser = reqparse.RequestParser()
        parser.add_argument('api_key',required=True)
        parser.add_argument('name',required=True)
        parser.add_argument('password',required=True)
        parser.add_argument('companyName',required=True)
        parser.add_argument('companyDescribtion',required=False)
        parser.add_argument('overview',required=False)
        parser.add_argument('links',required=False)
        parser.add_argument('Logo',required=False)
        args = parser.parse_args()
        profile = check_api_key
        if not profile:
            return jsonify('error : api_key invalid')
        def update_data(table , dataName , value , id):
            if not value:
                return False
            sql = 'update company_profile set ' + dataName + ' = %s where id = '+ str(id)
            val = (value,) 
            mycursor.execute(sql,val)
        for i in args:
            update_data('company_profile',i,args[i],user_data[0][0])
        mydb.commit()
    
    
    
    
    
