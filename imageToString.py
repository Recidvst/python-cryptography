import base64
import hashlib
import pyperclip
import sys

if len(sys.argv) > 1:
    openFile = sys.argv[1]
    writeFile = sys.argv[2] if len(sys.argv) > 2 else 'encodedImage.txt'
    
    try:
        with open(openFile, "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
            hashStr = hashlib.sha256(str).hexdigest()
            pyperclip.copy(hashStr)
            print(hashStr)

    except FileNotFoundError:
        sys.exit('Error: target file not found')

    try:
        with open(writeFile, "wb") as imageFile:
            imageFile.write(str)
            imageFile.close()
            
    except Exception:
        sys.exit('Error: write to file failed')

