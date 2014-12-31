__author__ = 'srv'
#Name: Sarvesh Sadhoo
#UTA ID: 1000980763
import boto.dynamodb
import csv
import time

# Create Connection to  AWS Dynamo DB
conn = boto.dynamodb.connect_to_region("us-east-1",
                        aws_access_key_id='',
                        aws_secret_access_key='')

trainingTable = conn.get_table('Training_Data')
testTable = conn.get_table('Test_Data')

#Start Timer
start = time.time()

# Function To Training Insert Data in Dynamo DB
def data_insert(UID, pclass, sex, age, parch, embarked, survived):
    # Create Json data format for insertion
    item_data = {
        'Pclass': pclass,
        'Sex': sex,
        'Age': age,
        'Parch': parch,
        'Embarked': embarked,
        'Survived': survived
    }
    # Insert Data
    item = trainingTable.new_item(
        hash_key=UID,
        range_key='',
        attrs=item_data
    )
    #Commit Data
    item.put()

# Parse the training data csv file
with open('train.csv', 'rU') as f:

    reader = csv.reader(f)
    next(reader, None)
    UID = 1
    for row in reader:
        #Get specific attributes from the training data csv file
        Sex = row[4]
        Age = row[5]
        Pclass = row[2]
        Parch = row[7]
        Embarked = row[11]
        Survived = row[1]
        if Survived == '0':
            Survived = 'No'
        elif Survived == '1':
            Survived = 'Yes'
        print UID, Pclass, Sex, Age, Parch, Embarked, Survived
        data_insert(UID, Pclass, Sex, Age, Parch, Embarked, Survived)
        UID += 1

elapsed = (time.time() - start)
print "Training Data Inserted In DynamoDB"
print elapsed
newStart = time.time()


# Function To Test Insert Data in Dynamo DB
def insert_test(UID, pclass, sex, age, parch, embarked):
    # Create Json data format for insertion
    item_data = {
        'Pclass': pclass,
        'Sex': sex,
        'Age': age,
        'Parch': parch,
        'Embarked': embarked,
    }

    # Insert Data
    item = testTable.new_item(
        hash_key=UID,
        range_key='',
        attrs=item_data
    )
    # Commit Data
    item.put()

# Parse the training data csv file
with open('test.csv', 'rU') as f:
    reader = csv.reader(f)
    next(reader, None)
    UID = 1
    #Get specific attributes from the training data csv file
    for row in reader:
        Sex = row[3]
        Age = row[4]
        Pclass = row[1]
        Parch = row[6]
        Embarked = row[10]
        print UID, Pclass, Sex, Age, Parch, Embarked
        insert_test(UID, Pclass, Sex, Age, Parch, Embarked)
        UID += 1

elapsed = (time.time() - newStart)
print "Test Data Inserted In DynamoDB"
print elapsed

