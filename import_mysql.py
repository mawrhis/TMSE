# import mysql module
import MySQLdb

# import regular expression module
import re

# set file name & location (note we need to create a temporary file because 
# the original one is messed up)

file = open('data.csv', 'r')
print "file opened"


# initialize & establish connection 
con = MySQLdb.connect(host="localhost",user="root", passwd="password",db="dbname") 
cur = con.cursor()
print "connected to the database"


# create a query 
query = 'load data local infile "data.csv" into table posts fields terminated by "," lines terminated by "\n" '
print "applying query"
# run it 
cur.execute(query)
print "querry executed"
# commit just in case 
con.commit()
print "finished"