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


class Jobs(Resource):
    def get(self):
        sql = ('select * from job')
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    def post(self):
        def check_api_key_company(email):
            sql = ('select * from company_profile where api_key = %s')
            val = (email,)
            mycursor.execute(sql,val)
            data = mycursor.fetchall()
            if len(data)<0:
                return False
            return data
        
        parser = reqparse.RequestParser()
        parser.add_argument('api_key',required=True)
        parser.add_argument('jobName',required=True)
        parser.add_argument('location',required=True)
        parser.add_argument('languageRequierment',required=True)
        parser.add_argument('experienceRequierment',required=True)
        parser.add_argument('skillNeeded',required=True)
        parser.add_argument('visaSponsorship',required=True)
        parser.add_argument('position',required=True)
        parser.add_argument('speciality',required=True)
        parser.add_argument('salaryRange',required=True)
        parser.add_argument('jobDescribtion',required=True)
        args = parser.parse_args()
        company_profile  = check_api_key_company(args['api_key'])
        if not company_profile:
            return jsonify("error : invalid api_key")
        sql = "insert into job (companyId ,jobName , location , languageRequierment,experienceRequierment,skillNeeded,visaSponsorship,position,speciality,salaryRange,jobDescribtion) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(
            company_profile[0][0],
            args['jobName'],
            args['location'],
            args['languageRequierment'],
            args['experienceRequierment'],
            args['skillNeeded'],
            args['visaSponsorship'],
            args['position'],
            args['speciality'],
            args['salaryRange'],
            args['jobDescribtion']
            )
        mycursor.execute(sql,values)
        mydb.commit()
        return True
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',required=True)
        args = parser.parse_args()
        sql = ('delete from job where id = ' + args['id'])
        mycursor.execute(sql)
        mydb.commit()
        return True



