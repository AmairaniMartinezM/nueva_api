import hashlib

passw = "123456"

hashtoken = hashlib.sha256(passw.encode()).hexdigest() 

print(hashtoken)