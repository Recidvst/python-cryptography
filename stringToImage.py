import base64
import sys

if len(sys.argv) > 1:
    openFile = sys.argv[1]
    writeFile = sys.argv[2] if len(sys.argv) > 2 else 'decodedImage.jpg'

    try:
        with open(openFile, 'rb') as imageFile:
            data = base64.b64decode(imageFile.read()) # decode from base64
            fi = open(writeFile, "wb") # open end image file to write to
            fi.write(data)
            fi.close()

    except FileNotFoundError:
        sys.exit('Error: target file not found or write to image file failed')

else : 
    sys.exit('Please provide a file containing a base64 encoded image as an argument')
