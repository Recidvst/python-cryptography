import base64
import sys

if len(sys.argv) > 1:
    openFile = sys.argv[1]
    writeFile = sys.argv[2] if len(sys.argv) > 2 else 'encodedImage.txt'
    
    try:
        with open(openFile, "rb") as imageFile:
            str = base64.b64encode(imageFile.read()) # encode as base64

    except FileNotFoundError:
        sys.exit('Error: target file not found')

    try:
        with open(writeFile, "wb") as imageFile:
            imageFile.write(str) # write base64 encoded image to new file
            
    except Exception:
        sys.exit('Error: write to file failed')

else : 
    sys.exit('Please provide an image file as an argument')