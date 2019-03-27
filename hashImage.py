import base64
import hashlib
import pyperclip
import sys

if len(sys.argv) > 1:
    openFile = sys.argv[1]
    
    try:
      # open provided file to encode and hash
        with open(openFile, "rb") as imageFile:
            str = base64.b64encode(imageFile.read()) # encode
            hashStr = hashlib.sha256(str).hexdigest() # hash
            pyperclip.copy(hashStr) # copy to clipboard
            print(hashStr)

    except FileNotFoundError:
        sys.exit('Error: target file not found')

else : 
    sys.exit('Please provide an image file as an argument')
