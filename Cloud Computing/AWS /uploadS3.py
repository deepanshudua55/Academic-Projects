# Name: Sarvesh Sadhoo
# UTA ID: 10000980763

# Import all the libraries
import os, math, time
from boto.s3.connection import S3Connection
from filechunkio import FileChunkIO

AWSAccessKeyId = ''
AWSSecretKey = ''

conn = S3Connection(AWSAccessKeyId, AWSSecretKey)
b = conn.get_bucket('srvcloud')

# Get file info
source_path = '/Users/srv/Desktop/hd2013.csv'
source_size = os.stat(source_path).st_size

# Create a multipart upload request
mp = b.initiate_multipart_upload(os.path.basename(source_path))

# Use a chunk size of 50 MiB (feel free to change this)
chunk_size = 52428800
chunk_count = int(math.ceil(source_size / chunk_size))

# Send the file parts, using FileChunkIO to create a file-like object
# that points to a certain byte range within the original file. We
# set bytes to never exceed the original file size.
start = time.clock()
for i in range(chunk_count + 1):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
     mp.upload_part_from_file(fp, part_num=i + 1)

elapsed = (time.clock() - start)
print elapsed

# Finish the upload
mp.complete_upload()