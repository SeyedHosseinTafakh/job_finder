# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 01:12:17 2020

@author: Hossein
"""

import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='jobFinder'
)

mycursor = mydb.cursor()

