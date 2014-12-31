#References:
#1. https://www.dropbox.com/developers/core/start/python
#2. http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
#3. http://www.saltycrane.com/blog/2011/10/python-gnupg-gpg-example/

#Name: Sarvesh Sadhoo
#UTA ID: 1000980763
#Course: Cloud Computing CSE6331
#Project: Cloud Project 1 (Dropbox)

# Import all the libraries
import os
import time
import dropbox
import gnupg

print "Drag and drop a file to upload!"

#Create An Instance Of GNUPG
gpg = gnupg.GPG()

# Create Encryption Key
input_data = gpg.gen_key_input(
    name_email='',
    passphrase='')
key = gpg.gen_key(input_data)
new_key = str(key)

#Convert the generated key in ascii format
public_key = gpg.export_keys(new_key) #Public key
private_key = gpg.export_keys(new_key, True) #Private Key
with open('keyrepo.asc', 'w') as f: #Create a file to store public & private key.
    f.write(public_key)
    f.write(private_key)

# Check for change in the folder
dir_path = "/Users/srv/Desktop/Code/Cloud Storage"
before_folder = dict([(f, None) for f in os.listdir(dir_path)])

# Returns the access token
def access_token():
    try:
        # Dropbox app key and secret from the Dropbox developer website
        app_key = ''
        app_secret = ''

        # Create a instance of the dropbox connection.
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        authorize_url = flow.start()
        print '1. Go to: ' + authorize_url
        print '2. Click "Allow" (you might have to log in first)'
        print '3. Copy the authorization code.'
        code = raw_input("Enter the authorization code here: ").strip()

        # This will fail if the user enters an invalid authorization code
        access_token, user_id = flow.finish(code)
        return access_token
    except:
        print "Error in access code. Try Again!"


# Upload the file to dropbox.
def upload(access_token, file_name, gpg):
    try:
        print "Path: ", os.getcwd()
        # Have the user sign in and authorize this token
        print "File to upload", file_name
        #print "Access Token", access_token

        # Create a instance of the dropbox connection.
        client = dropbox.client.DropboxClient(access_token)

        # Encrypt The File To Be Uploaded.
        enc_file_name = file_name + '.gpg'
        with open(file_name, 'rb') as upload_file:
            status = gpg.encrypt_file(
                upload_file, recipients=['sarveshsadhoo@gmail.com'],
                output=enc_file_name)

        print 'File Encrypted Successfully: ', status.ok
        f = open(enc_file_name, 'rb')
        response = client.put_file(enc_file_name, f)
        print 'File ' + enc_file_name + ' Uploaded: ', response

        if response:
            download(access_token, enc_file_name, gpg, file_name)
    except:
        print "Error in file uploading. Try Again!"


# Download the file ftom dropbox.
def download(access_token, enc_file_name, gpg, file_name):
    try:
        # Create a instance of the dropbox connection.
        client = dropbox.client.DropboxClient(access_token)
        # Change directory
        os.chdir('/Users/srv/Desktop/Code/Cloud Storage/Downloaded')

        f, metadata = client.get_file_and_metadata(enc_file_name)
        out = open(enc_file_name, 'wb')
        out.write(f.read())
        out.close()

        #Unencrypt the file
        with open(enc_file_name, 'rb') as f:
            status = gpg.decrypt_file(f, passphrase='my passphrase', output=file_name)

        print "File Downloaded: ", metadata
        print 'File Successfully Decrypted: ', status.ok
        os.chdir('/Users/srv/Desktop/Code/Cloud Storage')
    except:
        print "Error in downloading. Try Again"

# Remove the file from dropbox.
def remove(access_token, file_name):
    client = dropbox.client.DropboxClient(access_token)
    resp = client.file_delete(file_name)
    print "File Removed Successfully. Response: ", resp

while 1:
    time.sleep(10) # Wait for sometme to check for change
    after_folder = dict([(f, None) for f in os.listdir(dir_path)]) # Folder Status
    added_file = [f for f in after_folder if not f in before_folder] # Folder Status
    deleted_file = [f for f in before_folder if not f in after_folder]
    file_to_upload = ", ".join(added_file) # Get file name of added file
    file_to_remove = ", ".join(deleted_file) # Get file name of removed file

    # Check if a new file added
    if added_file and file_to_upload[-3:] != 'gpg':
        file_to_upload = ", ".join(added_file)
        print "New File Added:", ", ".join(added_file)
        token = access_token()
        upload(token, file_to_upload, gpg)

    # Check if a file is removed
    if deleted_file and file_to_remove[-3:] != 'gpg':
        file_to_remove = ", ".join(deleted_file)
        print "File To Be Removed:", ", ".join(deleted_file)
        token = access_token()
        file_to_remove += '.gpg'
        remove(token, file_to_remove)
        os.remove(file_to_remove)

    before_folder = after_folder