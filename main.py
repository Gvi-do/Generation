import hashlib

def hash_file(file):
    with open(file) as f:
        for line in f:
            line = hashlib.md5(b'line')
            yield line




for string in hash_file('Name.txt'):
    print(string)



