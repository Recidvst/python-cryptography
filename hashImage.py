import base64
import hashlib
import pyperclip
import sys
import os

# function - convert string to bytes for use in hash fn
def byter(string) :
    return bytes(string, encoding='utf-8')
# function - hash input with sha512 plus a manual salt
def hasher(string, salt) : 
    if isinstance(string, (bytes, bytearray)):
        return hashlib.sha512( string + byter(salt) ).hexdigest()
    else:
        return hashlib.sha512( byter(string) + byter(salt) ).hexdigest()
# function - hash input with sha512 plus a random salt
def randHasher(string) : 
    if isinstance(string, (bytes, bytearray)):
        return hashlib.sha512( string + os.urandom(10) ).hexdigest()
    else:
        return hashlib.sha512( byter(string) + os.urandom(10) ).hexdigest()

def mainHash(fileNamePassed='', saltPassed='') :
    # check if file passed when used as an import
    if fileNamePassed and len(fileNamePassed) > 0:
        openFile = fileNamePassed
    #  else user system args when called directly
    elif len(sys.argv) > 1:
        openFile = sys.argv[1]
    # exit if nothing passed
    else : 
        sys.exit('Please provide an image file as an argument')
        
    # check if a salt was passed when used as an import
    if saltPassed and len(saltPassed) > 0:
        salt = saltPassed
    #  else user system args when called directly
    else : 
        salt = sys.argv[2] if len(sys.argv) > 2 else 'secret-salt'

    try:
        # open provided file to encode
        with open(openFile, "rb") as imageFile:
            encodeString = base64.b64encode(imageFile.read()) # encode as base64

        # hash with sha512 + salt
        hashStr = hasher(encodeString, salt) 

        # then hash 999 times (stretching) with random salts
        for i in range(999) : 
            hashStr = randHasher(hashStr)

        pyperclip.copy(hashStr) # copy to clipboard
        print('Image as hash -> ' + hashStr)

    except FileNotFoundError:
        sys.exit('Error: target file not found')


if __name__ == "__main__":
    mainHash()