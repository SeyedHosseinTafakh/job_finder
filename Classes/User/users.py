# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:01:17 2020

@author: Hossein
"""

import pandas as pd
import numpy as np
from flask_restful import Resource , reqparse
import werkzeug
from werkzeug.utils import secure_filename
from flask import jsonify ,request
from connector import *
from flask import jsonify

ALLOWED_EXTENSIONS = set(['pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def check_email(email):
    sql = ('select * from user where email = %s')
    val = (email,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if len(data)>0:
        return False
    return True
def check_api_key(email):
    sql = ('select * from user where api_key = %s')
    val = (email,)
    mycursor.execute(sql,val)
    data = mycursor.fetchall()
    if len(data)<0:
        return False
    return data
def update_data(table , dataName , value , id):
    if not value:
        return False
    sql = 'update user set ' + dataName + ' = %s where id = '+ str(id)
    val = (value,)
    mycursor.execute(sql,val)

class User(Resource):
    def get(self):
        sql = 'select * from user'
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    def post(self):
        if 'ResumeFile' not in request.files:
            resp = jsonify({"message":{'ResumeFile' : 'Missing required parameter in the JSON body or the post body or the query string'}})             
            resp.status_code = 400
            return resp
        file = request.files['ResumeFile']
        if not allowed_file(file.filename):
            resp = jsonify({"message":{'ResumeFile' : 'File format is not acceptable , acceptable foramtes = '+str(ALLOWED_EXTENSIONS)}})             
            resp.status_code = 400
            return resp
        parser = reqparse.RequestParser()
        parser.add_argument('FirstName',required=True)
        parser.add_argument('LastName',required=True)
        parser.add_argument('Gender',required=False)
        parser.add_argument('Country',required=False)
        parser.add_argument('BirthDate',required=False)
        parser.add_argument('BlueCard',required=False)
        #parser.add_argument('FILE',required=True)
        #parser.add_argument('ResumeFile', type=werkzeug.FileStorage, location='Files',required=True)
        parser.add_argument('workExperience',required=False)
        parser.add_argument('SalaryRequired',required=False)
        parser.add_argument('TargetedCountries',required=False)
        parser.add_argument('Languages',required=False)
        parser.add_argument('email',required=True)
        parser.add_argument('Address',required=False)
        parser.add_argument('password',required=True)
        parser.add_argument('job_sector',required=False)

        

        parser.add_argument('skills',required=False)
        args = parser.parse_args()
        #checking for email
        mail_check = check_email(args['email'])    
        if not mail_check:
            return jsonify("error : email already exist")
        
        
        
        
        sql = "INSERT INTO user (firstName, lastName , gender,country,BirthDate,blueCard,targetedCountries,languages,address,email,password,api_key,job_sector,workExperience,skills,SalaryRequired,resumeAddress) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (args['FirstName'],
               args['LastName'],
               args['Gender'],
               args['Country'],
               args['BirthDate'],
               args['BlueCard'],
               args['TargetedCountries'],
               args['Languages'],
               args['Address'],
               args['email'],
               args['password'],
               'api_key',
               args['job_sector'],
               args['workExperience'],
               args['skills'],
               args['SalaryRequired'],
               'file_name'#todo :: have to manage file names
               )
        mycursor.execute(sql, val)
        mydb.commit()
        return args

class logIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email',required=True)
        parser.add_argument('password',required=True)
        args = parser.parse_args()
        sql = ('select * from user where email = %s and password = %s')
        val = (args['email'],args['password'])
        mycursor.execute(sql, val)
        data = mycursor.fetchall()
        return jsonify(data)
        
        
class update_user(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('api_key',required=True)
        parser.add_argument('firstName',required=False)
        parser.add_argument('lastName',required=False)
        parser.add_argument('gender',required=False)
        parser.add_argument('country',required=False)
        parser.add_argument('birthDate',required=False)
        parser.add_argument('blueCard',required=False)
        parser.add_argument('workExperience',required=False)
        parser.add_argument('salaryRequired',required=False)
        parser.add_argument('targetedCountries',required=False)
        parser.add_argument('languages',required=False)
        parser.add_argument('address',required=False)
        parser.add_argument('job_sector',required=False)
        parser.add_argument('skills',required=False)
        #have to handle resume file
        args = parser.parse_args()
        user_data = check_api_key(args['api_key'])
        if not user_data:
            return jsonify('error : api_key not valid')
        del(args['api_key'])
        
        for i in args:
            update_data('user',i,args[i],user_data[0][0])
        mydb.commit()
        #------------------------------------------------
        
        return jsonify(True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        