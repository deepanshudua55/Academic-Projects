#http://stackoverflow.com/questions/10592480/sort-a-dictionary-of-dictionaries-python

import sys
import csv
import time
import datetime


# File input paths to the main program provided by the user.
try:
    users_file_path = sys.argv[1]
    user2_file_path = sys.argv[2]
    job_file_path = sys.argv[3]
    apps_file_path = sys.argv[4]
    output_file_path = sys.argv[5]
except:
    print 'Incorrect File Path Provided'
    sys.exit(0)

#Start timer for calculating program execution time
start_time = time.time()
print '\n'
print "Program Execution Started Successfully"
#--------------------------------------------------------------------------------------------------


# Return value of this method is a hash table with attributes of all the users in users.tsv
def parse_users_tsv(file_path):
    #Hash Map for user data
    user_data_hash = {}
    #Open and read data from users.tsv
    file_open = open(file_path, "rb")
    reader = csv.reader(file_open, dialect="excel", delimiter="\t", quoting=csv.QUOTE_NONE)
    reader.next()
    for row in reader:
        #User's attributes selected
        user_id = int(row[0])
        state = row[2]
        country = row[3]
        degree = row[5]
        major = row[6]
        experience = row[9]
        current_employed = row[10]
        #Check if user is not in user_data_hash
        if user_id not in user_data_hash:
            user_data_hash[user_id] = [state, country, degree, major, experience, current_employed]

    return user_data_hash

user_data_hash = parse_users_tsv(users_file_path)
#--------------------------------------------------------------------------------------------------


#Create a list of user id present in users2.tsv
def parse_users2(file_path):
    users2_list = []
    file_open=open(user2_file_path, "rb")
    reader = csv.reader(file_open, dialect="excel", delimiter="\t", quoting=csv.QUOTE_NONE)
    for row in reader:
        users_id = int(row[0])
        users2_list.append(users_id)
    return users2_list

users2_list = parse_users2(user2_file_path)
#--------------------------------------------------------------------------------------------------


# Calculate the similarity score of users in user2.tsv and users in users.tsv
def similarity_score(user_data_hash):
    user2_score_hash = {}
    for user2 in users2_list:
        user2_data = user_data_hash[user2]
        state2 = user2_data[0]
        country2 = user2_data[1]
        degree2 = user2_data[2]
        major2 = user2_data[3]
        experience2 = user2_data[4]
        employed2 = user2_data[5]

        for user in user_data_hash:
            if user2 != user:
                score = 0
                user_data = user_data_hash[user]
                state = user_data[0]
                country = user_data[1]
                degree = user_data[2]
                major = user_data[3]
                experience = user_data[4]
                employed = user_data[5]

                # Assign score for every attribute that matches.
                if state2 == state and state2 != '' and state != '':
                    score += 1
                if country2 == country and country2 != '' and country != '':
                    score += 2
                if degree2 == degree and degree != '' and degree2 != '':
                    score += 1
                if major2 == major and major != '' and major2 != '':
                    score += 1
                if experience2 == experience and experience != '' and experience2 != '':
                    score += 1
                if employed2 == employed and employed != '' and employed2 != '':
                    score += 1

                if user2 not in user2_score_hash and score >= 3:
                    user2_score_hash[user2] = {score: [user]}

                elif user2 in user2_score_hash and score >= 3:
                    user2_internal_hash = user2_score_hash[user2]
                    if score not in user2_internal_hash:
                        user2_internal_hash[score] = [user]
                    elif score in user2_internal_hash:
                        user2_internal_hash[score].append(user)

    return user2_score_hash

users2_score_data = similarity_score(user_data_hash)
#--------------------------------------------------------------------------------------------------


# Keep top 2 weight for each user and drop other lower score users
def reduce_score(users2_score_data):
    for uid in users2_score_data:
        inner = users2_score_data[uid]
        flag = 0
        for score in sorted(inner.keys(), reverse=True):
            if score == 7:
                flag += 1
            elif score == 6:
                flag += 1
            elif score == 5:
                if flag == 2:
                    del inner[score]
                flag += 1
            elif score == 4:
                if flag == 2:
                    del inner[score]
            elif score == 3:
                if flag == 2:
                    del inner[score]
                flag += 1
    return users2_score_data

user2_reduced_score = reduce_score(users2_score_data)
#--------------------------------------------------------------------------------------------------
'''Parse jobs.tsv and get JobId that have end date after 2012-04-09 00:00:00'''


# Return boolean for comparing two date time values
def check_data(jobEndDate):

    year = int(jobEndDate[0:4].lstrip('0'))
    month = int(jobEndDate[5:7].lstrip('0'))
    date = int(jobEndDate[8:10].lstrip('0'))
    hour = int(jobEndDate[11:13].lstrip('0'))
    minute = int(jobEndDate[14:16].lstrip('0'))
    second = int(jobEndDate[17:19].lstrip('0'))

    return datetime.datetime(year, month, date, hour, minute, second) > \
            datetime.datetime(2012, 04, 9, 00, 00, 00)


# Parse jobs file with only job id with in defined end date.
def parse_jobs(file_path):
    job_hash = {}
    file_open = open(file_path, "rb")
    reader = csv.reader(file_open, dialect="excel", delimiter="\t", quoting=csv.QUOTE_NONE)
    reader.next()
    for line in reader:
        jobID = line[0]
        jobEndDate = line[-1:][0]
        dateCheck = check_data(jobEndDate)

        if jobID not in job_hash and dateCheck:
            #Job end date is just used to put values in a Hash Table.
            job_hash[jobID] = jobEndDate

    return job_hash

job_hash = parse_jobs(job_file_path)
#--------------------------------------------------------------------------------------------------


#Parse apps.tsv and for every user id it contains a list of all job ids.
def parse_apps(file_path, job_hash):
    hash_apps = {}
    file_open = open(file_path, "rb")
    reader = csv.reader(file_open, dialect="excel", delimiter="\t",quoting=csv.QUOTE_NONE)
    reader.next()
    for line in reader:
        jobID = line[2]
        user_id = line[0]

        if jobID in job_hash:
            if user_id not in hash_apps:
                hash_apps[user_id] = [jobID]
            elif user_id in hash_apps:
                hash_apps[user_id].append(jobID)

    return hash_apps

hash_app = parse_apps(apps_file_path, job_hash)
#--------------------------------------------------------------------------------------------------


# Get Job Ids for the user id.
def userid_jobid_mapping(user2_reduced_score, hash_apps):
    for user2 in user2_reduced_score:
        score_hash = user2_reduced_score[user2]

        for score in score_hash:
            user_id_list = score_hash[score]
            job_list = []

            for uid in user_id_list:
                if str(uid) in hash_apps:
                    # Get users list of job id that he applied to.
                    user_job_list = hash_apps[str(uid)]
                    if 601021 in user_job_list:
                        print "Check:", uid, user_job_list
                    job_list = job_list + user_job_list

            user2_reduced_score[user2][score] = job_list
    return user2_reduced_score

user2_reduced_score = userid_jobid_mapping(user2_reduced_score, hash_app)
#--------------------------------------------------------------------------------------------------


# Calculate the frequency of a JobId in the JobId list.
def counter(input_list):
    count_hash = {}
    for item in input_list:
        count_hash[item] = count_hash.get(item, 0) + 1
    return count_hash


# Count the occurrence of the job in the list and return hash with jobid: count
def frequency(user2_reduced_score):
    for userid in user2_reduced_score:
        score_hash = user2_reduced_score[userid]

        for score in score_hash:
            jobid_list = score_hash[score]
            new_hash = counter(jobid_list)
            user2_reduced_score[userid][score] = new_hash

    return user2_reduced_score

user2_reduced_score = frequency(user2_reduced_score)
#--------------------------------------------------------------------------------------------------


# Multiply score with occurrence to get final score value.
def final_score(user2_reduced_score):
    final_score_hash = {}
    for uid in user2_reduced_score:

        for score in user2_reduced_score[uid]:

            for jobid in user2_reduced_score[uid][score]:
                mul_score = user2_reduced_score[uid][score][jobid] * score

                if uid not in final_score_hash:
                    final_score_hash[uid] = {mul_score: [jobid]}
                elif uid in final_score_hash:
                    if mul_score not in final_score_hash[uid]:
                        final_score_hash[uid][mul_score] = [jobid]
                    elif mul_score in final_score_hash[uid]:
                        final_score_hash[uid][mul_score].append(jobid)
    return final_score_hash

final_score_hash = final_score(user2_reduced_score)
#--------------------------------------------------------------------------------------------------


# Compute Top Score for a User
def top_score(final_score_hash):

    top_score_hash = {}
    for uid in final_score_hash:
        inner_hash = final_score_hash[uid]
        max_score = max(inner_hash.keys())
        put_list = final_score_hash[uid][max_score]

        if uid not in top_score_hash:
            top_score_hash[uid] = {max_score:put_list}

    return top_score_hash

top_score_hash = top_score(final_score_hash)

#--------------------------------------------------------------------------------------------------
#Sort the Hash Table with the score as the key.
items = ((uid, job_list, score) for uid in top_score_hash for score, job_list in top_score_hash[uid].items())
ordered = sorted(items, key=lambda x: x[-1], reverse=True)

# Write top 150 UserID and JobID with score as the distinguishing attribute.
def output_write(ordered, file_path):
    fo = open(file_path, "wb")
    count = 0
    for data in ordered:
        uid = data[0]
        job_list = data[1]
        for job in job_list:
            if count < 150:
                fo.write(str(uid) + '\t')
                fo.write(str(job) + '\t' + '\n')
                count += 1
            else:
                break

output_write(ordered, output_file_path)
print "Program execution finished, output written to output.tsv file"
#--------------------------------------------------------------------------------------------------
end_time = time.time()
print "Elapsed Time: ", end_time - start_time


