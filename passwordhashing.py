import hashlib
import os
#Hash a password using SHA-256 with a salt.
def hash_password_sha256(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.sha256(salt + password).hexdigest()
    return salt.encode('hex') + hashed
# Verify a password against the stored SHA-256 hash.
def verify_password_sha256(password, stored_hash):
    salt = stored_hash[:32].decode('hex')
    stored_password_hash = stored_hash[32:]
    return hashlib.sha256(salt + password).hexdigest() == stored_password_hash
password = raw_input("Enter your password: ")
hashed_password = hash_password_sha256(password)
print("Stored Hash:", hashed_password)
# Verify password
if verify_password_sha256(password, hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect!")
