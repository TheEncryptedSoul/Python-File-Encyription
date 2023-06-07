import os
import cryptography
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = Fernet(key).encrypt(original_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

key = b'L0LbPSjj+y6kBy+94vYZ0JdtJeUYVgOifyKmv3PmSPk='  # Replace this with your preferred encryption key

# Example usages:
encrypt_file('C:\\Users\\Korisnik\\Desktop\\Sajtovi\\file encrypt\\File after encryption.txt', key)
#decrypt_file('', key)
#encrypt_folder('path/to/folder', key)
#decrypt_folder('path/to/folder', key)
