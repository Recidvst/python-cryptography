import hashlib
import itertools
import copy

#  hash formatter
def byter(string) :
    return bytes(string, encoding='utf-8')
def hasher(string) : 
    return hashlib.sha224(byter(string)).hexdigest()

# digits to try
digits = '12345'

# target hash
target = hasher('32451')
print('Target hash = ' + target)

# action 
results = [''.join(i) for i in itertools.permutations(digits, 5)]

for i in results :
    h = hasher(i)
    if h == target :
        print('Success!')
        print('Password = ' + i)
