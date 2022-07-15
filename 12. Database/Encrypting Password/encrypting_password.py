import bcrypt
password = b"abc123"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

pwd = bcrypt.checkpw(password, hashed)
print(pwd)

if bcrypt.checkpw(password, hashed):
    print("Password matched")
else:
    print("Wrong password")
