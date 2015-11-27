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
actor_id = 0
movie_id = 0

cast = []

connection_ub = connection.MySQLConnection (user='user', password='12345678', host='mysql-instance.ctyplruqgzr3.us-east-1.rds.amazonaws.com', database='mydb')
cursor_ub = connection_ub.cursor()

for tuple_ in list_movies :
    # converting each tuple to dictionary
    # print each_tuple_business
    tuple_ = tuple_.encode('ascii','ignore')
    movie_data = json.loads(tuple_)
    index = index + 1
    if (index % 100 == 0) :
        print "===== In Index " + str(index) + "=================="
    for key in movie_data.keys() :
        if (key == "id") :
            movie_id = movie_data[key]
        if (key == "cast") :
            cast = movie_data[key]
    for actor in cast :
        for actor_key in actor.keys() :
            if (key == "personId") :
                actor_id = actor[key]
            sql_insert = ("INSERT INTO acts(actor_id, movie_id) VALUES (%s,%s)")
            cursor_ub.execute(sql_insert, (actor_id, movie_id))
    
connection_ub.commit()
connection_ub.close()
