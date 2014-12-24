# Name: Sarvesh Sadhoo
# UTA ID: 1000980763

import csv
import re
import time
import string
import sys
import random
import similarity_compute
from stemming.porter2 import stem
from stop_word import stop_word_hash

print "Program Execution Started"

try:
    jobs_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    jobs_file_path += 'jobs.tsv'
except:
    print 'Incorrect File Path Provided'
    sys.exit(0)

# Start execution timer.
start_time = time.time()


# Method to clean data.
def clean_data(data):
    junk_data = {'\r': ' ', '\n': ' ', '&nbsp': ' ', '\t': ' '}
    # Remove HTML formatiitng.
    new_data = re.compile(r'<.*?>')
    new_data = new_data.sub('', data)
    # Remove junk values
    for i, j in junk_data.iteritems():
        new_data = new_data.replace(i.encode('string-escape'), j)
    # Remove special characters
    new_data = re.sub('[^A-Za-z0-9\.]+', ' ', new_data)
    # Remove double spaces
    new_data = re.sub(' +', ' ', new_data)
    # Remove punctuations
    if sys.version_info < (2, 6):
        table = ''.join(chr(i) for i in xrange(256))
    else:
        table = None
    new_data = new_data.translate(table, string.punctuation)
    # Remove any digit from the sting
    new_data = ''.join([i for i in new_data if not i.isdigit()])
    return new_data

#-------------------------------------------------------------------------------------------


# Method to parse the data in the file and feed it to clean_data method.
def clean_data_hash(file_path):
    cl_data_hash = {}
    file_open = open(file_path, "rb")
    reader = csv.reader(file_open, dialect="excel", delimiter="\t", quoting=csv.QUOTE_NONE)
    reader.next()
    job_id_list = []
    for line in reader:
        job_id = line[0]
        desc_data = line[1]
        req_data = line[2]
        job_id_list.append(job_id)
        job_data = desc_data + req_data
        data = clean_data(job_data)
        final_data = data.split()

        if job_id not in cl_data_hash:
            cl_data_hash[job_id] = final_data

    return cl_data_hash, job_id_list

#jobs_file_path = '/Users/srv/Desktop/Code/DataMining3/jobs_cut100.tsv'
init_data_hash, job_id_list = clean_data_hash(jobs_file_path)
#-------------------------------------------------------------------------------------------


# Method removes stop words and performs stemming operation
def remove_stop_word(init_data_hash, stop_word_hash):
    # Remove stop word from the data set and perform stemming
    for job_id in init_data_hash:
        new_data_set = []
        for str_val in init_data_hash[job_id]:
            to_check = str_val.lower()
            if to_check not in stop_word_hash:
                new_data_set.append(stem(to_check))

        #Replace the old list for hash table with new list
        if job_id in init_data_hash:
            init_data_hash[job_id] = new_data_set

    return init_data_hash

# Data Cleaning/Stemming/Stop Words Removal Done Twice.
initial_clean_data = remove_stop_word(init_data_hash, stop_word_hash)
final_clean_data = remove_stop_word(initial_clean_data, stop_word_hash)
#-------------------------------------------------------------------------------------------


# Calculate frequency of stemmed words.
def stem_frequency(final_clean_data):
    for job_id in final_clean_data:
        word_list = final_clean_data[job_id]
        freq_hash = {}
        for word in word_list:
            if word not in freq_hash:
                freq_hash[word] = 1
            elif word in freq_hash:
                freq_hash[word] += 1

        if job_id in final_clean_data:
            final_clean_data[job_id] = freq_hash

    return final_clean_data

# Count Matrix Hash Map Contains Frequency Count For JobID
count_matrix = stem_frequency(final_clean_data)
#------------------------------------------------------------------------------------


# Function computes similarity score between each JobID
def get_similarity_compute(count_matrix):
    job_id_list = count_matrix.keys()
    random_list = random.sample(job_id_list, 10)
    centroid_hash = {}

    for job_id in count_matrix:
        init_value = 0
        for jid in random_list:
            if job_id != jid:
                m1 = count_matrix[job_id]
                m2 = count_matrix[jid]
                similarity_value = similarity_compute.get_similarity(m1, m2)
                if init_value < similarity_value:
                    init_value = similarity_value
                    temp = jid

        # Create a centroid hash containing  jobid in the centroid
        if temp not in centroid_hash and temp != job_id:
            centroid_hash[temp] = {job_id: init_value}
        elif temp in centroid_hash:
            if job_id not in centroid_hash:
                centroid_hash[temp][job_id] = init_value

    # Check for any duplicate centroid in same hash
    for j in centroid_hash:
        for job in centroid_hash:
            if j != job:
                if str(job) in centroid_hash[j]:
                    del centroid_hash[j][str(job)]

    return centroid_hash
#------------------------------------------------------------------------------------

# Main functions computes best cluster for multiple iterations
def main(count_matrix):
    loop_counter = 0
    max_similarity_val = 0
    max_cluster_hash = {}
    while loop_counter != 50:
        cluster_hash = get_similarity_compute(count_matrix)
        similarity_sum = 0
        for job_id in cluster_hash:
            similarity_sum += sum(cluster_hash[job_id].values())
            #print job_id, cluster_hash[job_id]
        if similarity_sum > max_similarity_val:
            max_similarity_val = similarity_sum
            max_cluster_hash = cluster_hash

        loop_counter += 1

    return max_similarity_val, max_cluster_hash

max_similarity_val, max_cluster_hash = main(count_matrix)
#---------------------------------------------------------------------------------------------
# Compute Cluster Hash
cluster_hash = {}
cluster_count = 1
for job in max_cluster_hash:
    cluster_hash[cluster_count] = max_cluster_hash[job].keys()
    cluster_hash[cluster_count].append(job)
    cluster_count += 1

val_count = 0
for c in cluster_hash:
    val_count += len(cluster_hash[c])

# Compute Main Hash For Clustering
main_cluster_hash = {}
for cluster_id in cluster_hash:
    inner_job_list = cluster_hash[cluster_id]

    for jid in inner_job_list:
        if jid not in main_cluster_hash:
            main_cluster_hash[jid] = cluster_id
        else:
            print 'Raise Error'
#---------------------------------------------------------------------------------------------

# Write to output file
fo = open(output_file_path, "wb")

for job in job_id_list:
    fo.write(str(job) + '\t')
    fo.write(str(main_cluster_hash[job]) + '\t' + '\n')

print "Program Executed Successfully."
print "Output File Generated"
print "Time Elapsed:", time.time() - start_time