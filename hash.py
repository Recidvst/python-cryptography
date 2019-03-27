import hashlib

#  hash formatter
def byter(string) :
    return bytes(string, encoding='utf-8')
def hasher(string, salt) : 
    return hashlib.sha512( byter(string) + byter(salt) ).hexdigest()

salt='secret-salt'

string = "Hello World"
hashedString = hasher(string, salt)

# hash 100 times (stretching)
for i in range(100) : 
    hashedString = hasher(hashedString, salt)
    print(i+1, hashedString)

