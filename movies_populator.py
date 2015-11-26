# for converting json to dictionary
import json
# for connecting to MySQL component
import mysql.connector
from mysql.connector import errorcode
from pprint import pprint
from mysql.connector import (connection)
# import MySQLdb
from decimal import Decimal

# code to read data from JSON file in local machine into a dictionary
input_file = open("TMDBMovieInfo")
# ignoring encoding
file_data = input_file.read() # .encode('ascii', 'ignore')
# splitting json file on \n to access each json
list_movies = file_data.split('\n')
index = 0

# initializing values
movie_id = 0
title = ""
revenue = 0
budget = 0
adult = 0
user_rating = 0.0

connection_ub = connection.MySQLConnection (user='user', password='12345678', host='mysql-instance.ctyplruqgzr3.us-east-1.rds.amazonaws.com', database='mydb')
cursor_ub = connection_ub.cursor()

for tuple_ in list_movies :
    # converting each tuple to dictionary
    # print each_tuple_business
    tuple_ = tuple_.encode('ascii','ignore')
    movie_data = json.loads(tuple_)
    index = index + 1
    if (index % 500 == 0) :
        print "===== In Index " + str(index) + "=================="
    for key in movie_data.keys() :
        if (key == "id") :
            movie_id = movie_data[key]
        if (key == "title") :
            title = movie_data[key].strip()
        if (key == "revenue") :
            revenue = movie_data[key]
        if (key == "budget") :
            budget = movie_data[key]
        if (key == "adult") :
            adult = movie_data[key]
            '''if (movie_data[key]) :
                adult = 1
            else:
                adult = 0'''
        if (key == "userrating") :
            user_rating = movie_data[key]
    
    sql_insert = ("INSERT INTO movies(movie_id, title, revenue, budget, adult, user_rating) VALUES (%s,%s,%s,%s,%s,%s)")
    cursor_ub.execute(sql_insert, (movie_id, title, revenue, budget, adult, user_rating))
    
connection_ub.commit()
connection_ub.close()
