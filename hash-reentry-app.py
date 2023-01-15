# libraries
from hashlib import sha256

# greet user and ask for what password they'd like to set
print ('Hello, this demo will ask for a plaintext password, hash it and will verify the hash for access requests. For reference, a hash is a scrambled consistent alphanumeric version of a plaintext password. For example, the hash of "Jay" is: 0c9ab8c55d678ea513149008ce0ca19990aabc50f6bde84189031dad16079780')

# store the first hash as a variable
hash1 = (sha256(input('What password would you like to set? ').encode('utf-8'))).hexdigest()

# print message saying password hash has been stored
print ('Your password hash has been successfully stored.')

# promt the user for re-entry of password, hash then store as another var
hash2 = (sha256(input('I will test your hash. Please type your password: ').encode('utf-8'))).hexdigest()

# if same: access approved, else: access denied
while True:
    if hash1 == hash2:
        print('Success - password hash matches.')
        print('This has been a basic demo of how plaintext passwords can be stored as hashes, with the hash verified. In the real world, databases can store hashes which improves user security. As sha256 hashes have been shown to take longer to decrpt than the lifetime of the universe, hackers who obtain hashed passwords would not be able to gain the plaintext password required for login.')
        break
    else:
        print('The password hash does not match. Please run the programme again.')
        break