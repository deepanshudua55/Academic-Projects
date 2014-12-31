# Name: Sarvesh Sadhoo
# UTA ID: 10000980763

#Import all the libraries
import csv
import boto.rds
import MySQLdb

#Create a connection to AWS RDS
conn = boto.rds.connect_to_region("us-east-1",
                                  aws_access_key_id='',
                                  aws_secret_access_key='')

# Connect to AWS Instance
instances = conn.get_all_dbinstances()
db = instances[0]

#cont = MySQLdb.connect("localhost","root","password","DB")
db_conn = MySQLdb.connect("sarveshsadhoo.cjt8btmkkhjp.us-east-1.rds.amazonaws.com"
                       ,"username","password","innodb")

# Create cursonr for database connection
cursor1 = db_conn.cursor()
cursor2 = db_conn.cursor()

# SQL statement to get data from university and percapita table
sql1 = "SELECT * FROM university"
sql2 = "SELECT * FROM percapita"


# Function to get data using the above SQL Queries
def uni_data (cursor1, sql1):
    hashUni = {} # HashTable used to store university data
    try:
       # Execute the SQL command
       cursor1.execute(sql1)
       # Fetch all the rows in a list of lists.
       results = cursor1.fetchall()
       for row in results:
           state_abr = row[2]
           if state_abr not in hashUni:
               hashUni[state_abr] = 1
           else:
               hashUni[state_abr] += 1

    except:
       print "Error: unable to fecth data"

    return hashUni

# Function to get data from percapita income
def percap_data(cursor2, sql2):
    hashpercap = {} #HasTable used to store percapita data
    try:
       # Execute the SQL command
       cursor2.execute(sql2)
       # Fetch all the rows in a list of lists.
       results = cursor2.fetchall()
       for row in results:
           state_abr = row[1]
           if state_abr not in hashpercap:
               hashpercap[state_abr] = [row[0], row[2],row[3]]

    except:
       print "Error: unable to fetch data"

    return hashpercap

# Get the returened value from the function.
uni_data = uni_data (cursor1, sql1)
percap_data = percap_data(cursor2, sql2)

for item in percap_data:
    no_of_col = uni_data.get(item)
    percap_data[item].append(no_of_col)

# Create a cvs file from the University and Percapita Income data to represent in a bar chart
with open('mycsvfile.csv','wb') as f:
    w = csv.writer(f)
    state_tup = [] # State Name
    state_percap = [] # State Per Capita Income
    state_rank = [] # State Per Capita Income Rank
    state_no_uni = [] # Number of universities in a state
    for item in percap_data.values():
        state_tup.append(item[0])
        state_percap.append(item[1])
        state_rank.append(item[2])
        state_no_uni.append(item[3])

    # Convert to tuple for writing to file
    state_set = tuple(state_tup)
    percap_set = tuple(state_percap)
    rank_set = tuple(state_rank)
    count_set = tuple(state_no_uni)

    # Write operations
    w.writerow(state_set)
    w.writerow(percap_set)
    w.writerow(count_set)
    w.writerow(rank_set)

