import hashlib
t=input("Enter Input :")
r = hashlib.md5(t.encode())
print("This is md5 Hash :",r.hexdigest())