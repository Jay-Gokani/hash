# code to be cited in my article explaining how hashing works

# install sha256 library for hashing
from hashlib import sha256

# demo explanation
print ('Hello, this demo will ask for a plaintext password, hash it and will verify the hash for access requests. For reference, a hash is a deterministic scrambled alphanumeric version of a plaintext password. For example, the hash of "Jay" is: 0c9ab8c55d678ea513149008ce0ca19990aabc50f6bde84189031dad16079780')

# first hash stored as a variable
hash1 = (sha256(input('What phony password would you like to set? ').encode('utf-8'))).hexdigest()
print('The hash of your plaintext password is:', hash1)

# password hash stored confirmation
print ('Your password hash has been successfully stored.')

# promt the user for password re-entry, hash and store as another variable
hash2 = (sha256(input('I will test your hash. Please type your password: ').encode('utf-8'))).hexdigest()
print('The hash of your plaintext password is:', hash2)

# access approval or deny check
while True:
    if hash1 == hash2:
        print('Success - password hash matches.')
        print('This has been a basic demo of how plaintext passwords can be stored as hashes, with the hash verified. In the real world, databases can store hashes which improves user security. As sha256 hashes have been shown to take longer to decrpt than the lifetime of the universe, hackers who obtain hashed passwords would not be able to gain the plaintext password required for login.')
        break
    else:
        print('The password hash does not match. Please run the programme again.')
        break