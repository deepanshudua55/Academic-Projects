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

#Function to get training data from Dynamo DB
def get_training_data(conn):
    start = time.time()
    #Cretae connection with a specific table
    training_table = conn.get_table('Training_Data')
    #Open file for writing tab delimited data
    file_train = open('outputTraining.csv', 'wb')
    writer = csv.writer(file_train, dialect='excel-tab')
    writer.writerow(['pClass', 'Sex', 'Age', 'Embarked', 'Parch', 'Survived'])

    for i in range(1, 891):
        insert_list = []
        item = training_table.get_item(
            hash_key=i,
            range_key=None,
        )
        #Insert specific data into the tab delimited file.
        insert_list.append(item['Pclass'])
        insert_list.append(item['Sex'])
        insert_list.append(item['Age'])
        insert_list.append(item['Embarked'])
        insert_list.append(item['Parch'])
        insert_list.append(item['Survived'])
        print item['Pclass'], item['Sex'], item['Age'], item['Embarked'], item['Parch'], item['Survived']
        writer.writerow(insert_list)

    file_train.close()
    elapsed = (time.time() - start)
    print "Training Data Written Into Tab Delimited File"
    print elapsed


#Function to get training data from Dynamo DB
def get_test_data(conn):
    start = time.time()
    #Cretae connection with a specific table
    test_table = conn.get_table('Test_Data')
    #Open file for writing tab delimited data
    file_test = open('outputTest.csv', 'wb')
    writer = csv.writer(file_test, dialect='excel-tab')
    writer.writerow(['pClass', 'Sex', 'Age', 'Embarked', 'Parch'])

    for i in range(1, 418):
        insert_list = []
        item = test_table.get_item(
            hash_key=i,
            range_key=None,
        )
        #Insert specific data into the tab delimited file.
        insert_list.append(item['Pclass'])
        insert_list.append(item['Sex'])
        insert_list.append(item['Age'])
        insert_list.append(item['Embarked'])
        insert_list.append(item['Parch'])
        print item['Pclass'], item['Sex'], item['Age'], item['Embarked'], item['Parch']

        writer.writerow(insert_list)

    file_test.close()
    elapsed = (time.time() - start)
    print "Tested Data Written Into Tab Delimited File"
    print elapsed

#Function Call
get_training_data(conn)
get_test_data(conn)