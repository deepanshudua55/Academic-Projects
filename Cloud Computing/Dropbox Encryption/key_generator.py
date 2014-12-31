import gnupg

gpg = gnupg.GPG()
input_data = gpg.gen_key_input(
    name_email='',
    passphrase='')
key = gpg.gen_key(input_data)
new_key = str(key)

ascii_armored_public_keys = gpg.export_keys(new_key)
ascii_armored_private_keys = gpg.export_keys(new_key, True)
with open('mykeyfile.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)
