import csv, sys

# Set the csv file size limit to maximum size
csv.field_size_limit(sys.maxsize)

# File input paths to the main program and country name provided by the user.
country_name = sys.argv[1]
apps_path = sys.argv[2]
users_path = sys.argv[3]
jobs_path = sys.argv[4]
user_history_path = sys.argv[5]

print "-----------------------------Part One-------------------------------"

# Fucntions parse the users.tsv file and returns a hash map 
def parse_users_tsv(users_path):
    hash_user = {} #Hash Map for user data
    with open(users_path) as tsv: #Step 1
        tsv.next() #Skip the first line.
        for line in csv.reader(tsv, dialect="excel-tab"):
            user_id = line[0] #Get user ID
            if user_id not in hash_user:
                hash_user[user_id] = [line[2], line[3]] # Hash Map of the form {user_id: [state, country]}
    return hash_user

hash_user_input = parse_users_tsv(users_path) #Store the return value of the above fucntion.

# Fucntions parse the apps.tsv file and returns a hash map 
def parse_apps_tsv(hash_user_input,apps_path):
    hash_apps = {}
    with open(apps_path) as tsv: #Step 2
        tsv.next() #Skip the first line.
        for line in csv.reader(tsv, dialect="excel-tab"):
            jobID = line[2] #Get JOB ID
            userid_job = str(line[0]) #Get USER ID
            user_state = hash_user_input.get(userid_job)[0] #Get State ID from the above hash map
            #Create a hash map of hash map for Job ID as key and value as hash map cointaining
            #user_state and user_id
            if jobID not in hash_apps:
                hash_apps[jobID] = {user_state: [userid_job]}
            else:
                if user_state not in hash_apps[jobID]:
                    hash_apps[jobID][user_state] = [userid_job]
                else:
                    hash_apps[jobID][user_state].append(userid_job)
    return hash_apps

hash_apps_cube = parse_apps_tsv(hash_user_input, apps_path)

def max_apps_state(hash_table_apps_cube):
    #Get count of all the apps in a state 1019342 {'NJ': 1, 'PA': 5, 'DE': 1}
    # Get count for job applied for a particular Job ID
    for JobID in hash_table_apps_cube: #Step 3
        for list in hash_table_apps_cube[JobID]:
            hash_table_apps_cube[JobID][list] = len(hash_table_apps_cube[JobID][list])
    
    # Get the max application state 1019342 {'PA': 5}
    for inner_dic in hash_table_apps_cube: #Step 4
        # Max function gets the  
        top = max(hash_table_apps_cube[inner_dic], key=hash_table_apps_cube[inner_dic].get)
        value_top = hash_table_apps_cube[inner_dic].get(top)
        hash_table_apps_cube[inner_dic] = {top: value_top}

    return hash_table_apps_cube

hash_apps_max_cube = max_apps_state(hash_apps_cube)

# Calculates the top 5 state wise jobs applied.
print 'StateID'+'  '+'JobID'+'  '+'numOfApps'
counter = 0
while counter < 5:
    max_val = 0
    state = ''
    jobId = 0
    for dic in hash_apps_max_cube:
        for item in hash_apps_max_cube[dic]:
            job_count = hash_apps_max_cube[dic][item]
            if job_count > max_val:
                max_val = job_count
                state = item
                jobId = dic
    del hash_apps_max_cube[jobId]
    counter += 1
    print jobId, '  ', state, '   ', max_val

print "-----------------------------Part Two-------------------------------"
#-----------------------------------------------Part Two ------------------------------------------------

# Fucntions parse the apps.tsv file and returns a hash map 
def parse_apps_tsv_country(hash_user_input, apps_path):
    hash_apps_country = {}
    with open(apps_path) as tsv: #Step 2
        tsv.next()
        for line in csv.reader(tsv, dialect="excel-tab"):
            jobID = line[2]
            userid_job = str(line[0])
            user_state = hash_user_input.get(userid_job)[1]#Get Country ID from the above hash map
            #Create a hash map of hash map for Job ID as key and value as hash map cointaining
            #user_state and user_id
            if jobID not in hash_apps_country:
                hash_apps_country[jobID] = {user_state: [userid_job]}
            else:
                if user_state not in hash_apps_country[jobID]:
                    hash_apps_country[jobID][user_state] = [userid_job]
                else:
                    hash_apps_country[jobID][user_state].append(userid_job)
    return hash_apps_country

hash_apps_country_data = parse_apps_tsv_country(hash_user_input, apps_path)

# Fucntions parse the apps.tsv file and returns a hash map 
def parse_jobs(jobs_path):
    hash_jobs = {}
    with open(jobs_path) as tsv:
        #tsv.next()
        for line in csv.reader(tsv, dialect="excel-tab"):
            jobID = line[0]
            if jobID not in hash_jobs:
                hash_jobs[jobID] = line[1]
    return hash_jobs

parse_jobs_cube = parse_jobs(jobs_path)

# Count the number of applications for a particular Job ID
def apps_count(hash_apps_cube2):
    for job_id in hash_apps_cube2:
        for lists in hash_apps_cube2[job_id]:
            hash_apps_cube2[job_id][lists] = len(hash_apps_cube2[job_id][lists])
    return hash_apps_cube2

hash_apps_count_value = apps_count(hash_apps_country_data)

# Slice on the country given by the user to get data for a particular country
def slice_country_data(hash_apps_count_value, country_name):
    hash_slice_country = {}
    for jobID in hash_apps_count_value:
        for country in hash_apps_count_value[jobID]:
            if country == country_name:
                hash_slice_country[jobID] = hash_apps_count_value[jobID][country]
    return hash_slice_country

slice_country_data_count = slice_country_data(hash_apps_count_value, country_name)

# Group the jobs with same title and count them
def hash_title(parse_jobs_cube, slice_country_data_count):
    hash_title_count = {}
    for job_id in parse_jobs_cube:
        title = parse_jobs_cube[job_id] # Get title 
        count = slice_country_data_count.get(job_id) # Get count for Job IDs
        if count:
            if title not in hash_title_count:
                hash_title_count[title] = count
            else:
                hash_title_count[title] = hash_title_count[title] + count
    return hash_title_count

hash_title_count_value = hash_title(parse_jobs_cube, slice_country_data_count)

# Print the data as top 5 country wise job titles
print 'TitleID'+'    '+'numOfApps'
count = 0
for w in sorted(hash_title_count_value, key=hash_title_count_value.get, reverse=True):
    if count < 5:
        print w, ' ', hash_title_count_value[w]
    count += 1