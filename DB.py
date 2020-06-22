# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 05:54:28 2020

@author: Hossein
"""

import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)


mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE jobFinder CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='jobFinder'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE user (id INTEGER AUTO_INCREMENT PRIMARY key,firstName VARCHAR(255),lastName VARCHAR(255),gender VARCHAR(255),country VARCHAR(255),birthDate VARCHAR(255),blueCard VARCHAR(255),targetedCountries VARCHAR(255),languages VARCHAR(255),address VARCHAR (255) ,email VARCHAR (255) , password VARCHAR (255),api_key VARCHAR (255), job_sector VARCHAR (255) ,workExperience VARCHAR (255),skills VARCHAR (255), SalaryRequired VARCHAR (255),resumeAddress VARCHAR(255))")
#mycursor.execute("CREATE TABLE resume (id INTEGER AUTO_INCREMENT PRIMARY key,user_id VARCHAR(255))")
mycursor.execute("CREATE TABLE company_profile (id INTEGER AUTO_INCREMENT PRIMARY key,name VARCHAR(255),email VARCHAR (255) , password VARCHAR (255),api_key VARCHAR (255), companyName VARCHAR (255),companyDescribtion VARCHAR (255),overview VARCHAR (255),links VARCHAR (255),Logo VARCHAR (255))")
mycursor.execute("CREATE TABLE job (id INTEGER AUTO_INCREMENT PRIMARY key,companyId VARCHAR(255), jobName VARCHAR(255),location VARCHAR (255) , languageRequierment VARCHAR (255),experienceRequierment VARCHAR (255), skillNeeded VARCHAR (255),visaSponsorship VARCHAR (255),position VARCHAR (255),speciality VARCHAR (255),salaryRange VARCHAR (255),jobDescribtion VARCHAR (255))")


mycursor.execute("DROP DATABASE  jobFinder;")

mydb.commit()














