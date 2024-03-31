import base64, hashlib

def decode_base64_to_file(encoded_string, output_file):
    try:
        decoded_data = base64.b64decode(encoded_string)
        with open(output_file, 'wb') as f:
            f.write(decoded_data)
        # print("File decoded successfully!")
    except Exception as e:
        print("Error decoding file:", e)

# Specify the file you want to process here
with open('connector.gif', 'rb') as file:
    file_content = file.read()

# Encode file content to base64
base64_string = base64.b64encode(file_content).decode('utf-8')
print(base64_string)

# Call sha256 encryption method
hash_object = hashlib.sha256()
# Update the hash object with the string to be hashed
hash_object.update(base64_string.encode())

# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()

# Set the hash and point to position zero as the file name
file_name = hash_hex+"i0"

decode_base64_to_file(base64_string, file_name)
