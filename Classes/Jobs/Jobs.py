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



class Jobs(Resource):
    def get(self):
        return "hello World"
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('JobName',required=True)
        parser.add_argument('Location',required=True)
        parser.add_argument('LanguageRequierment',required=True)
        parser.add_argument('ExperienceRequierment',required=True)
        parser.add_argument('SkillNeeded',required=True)
        parser.add_argument('VisaSponsorship',required=True)
        parser.add_argument('Position',required=True)
        parser.add_argument('Speciality',required=True)
        parser.add_argument('SalaryRange',required=True)
        parser.add_argument('JobDescribtion',required=True)









