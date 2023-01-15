# import hashlib

# hash = (hashlib.sha256(input('password? ').encode('utf-8'))).hexdigest()
# print(hash)

from hashlib import sha256

hash = (sha256(input('password? ').encode('utf-8'))).hexdigest()
print(hash)