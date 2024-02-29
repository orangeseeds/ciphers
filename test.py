import sys
import os
import regex as re
import time
import transposition as cipher

def encrypt_file(file_name, string, key):
    encrypted_name = f"{file_name[0:-4]}.encrypted.txt"
    with open(encrypted_name, 'a') as f:
        f.write(cipher.encrypt(string, key))

def decrypt_file(file_name, string, key):
        encrypted_name = f"{file_name[0:-4]}.decrypted.txt"
        with open(encrypted_name, 'a') as f:
            f.write(cipher.decrypt(string, key))

def main(argv, argc):
    if argc == 4:
        key = int(re.findall('key=(\d+)',argv[3])[0])
        file = argv[2]
        with open(argv[2], 'r') as f:
            message = f.read()
        if argv[1] == '-e':
            print(f'Encrypting {file}...')
            start_time = time.time()
            encrypt_file(file, message, key)
            total_time = round(time.time() - start_time, 2)
            print(f'Encryption time: {total_time} seconds\n{file}({len(message)} characters) has been succesfully encrypted')
        elif argv[1] == '-d':
            print(f'Decrypting {file}...')
            start_time = time.time()
            decrypt_file(file, message, key)
            total_time = round(time.time() - start_time, 2)
            print(f'Decryption time: {total_time} seconds\n{file}({len(message)} characters) has been succesfully decrypted')
        else:
            print('Please specify if you want to encrypt(-e) or decrypt(-d) the file')
            return None
    else:
        print('Required number of arguements not met\n -e/-d "filename.txt" key=int')

if __name__ == '__main__':
    main(sys.argv , len(sys.argv))
