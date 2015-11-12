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
input_file = open("./yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json")
# ignoring encoding 
file_data = input_file.read() # .encode('ascii', 'ignore')
# splitting json file on \n to access each json
list_business = file_data.split('\n')
index = 0
# initializing values
business_id = ""
# attributes = ""
categories = ""

# dict_attributes = {}
# attr_id = 0

check_cat_list = []
category_id = 0

for each_tuple_business in list_business : 
	# converting each tuple to dictionary
	# print each_tuple_business
	each_tuple_business = each_tuple_business.encode('ascii','ignore')
	business_data = json.loads(each_tuple_business)
	index = index + 1
	print "===== In Index " + str(index) + "=================="
	str_value = "";
	subIndex = 0
	for each_key in business_data.keys() :
		if (each_key == "business_id") :
            business_id = business_data[each_key].strip()
        if (each_key == "categories") :
			for each_val in business_data[each_key] :
				if ( each_val not in check_cat_list ) :
					subIndex = subIndex + 1
					print "		Sub Index " + str(subIndex)
					check_cat_list.append(each_val)
					connection_ub = connection.MySQLConnection (user='urbanbeatsdb', password='urbanbeatsdbpwd', host='urbanbeats.czeuio4ikmlz.us-east-1.rds.amazonaws.com', database='UrbanBeatsDB')
					cursor_ub = connection_ub.cursor()
					category_id = category_id + 1
					sql_insert = ("INSERT INTO Categories(category_id, category_name) VALUES (%s,%s)")
					cursor_ub.execute(sql_insert, (category_id, each_val))
					connection_ub.commit()
					connection_ub.close()
