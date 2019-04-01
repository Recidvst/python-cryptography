import requests
from hashImage import mainHash

# GET random image from Unsplash API
url = "https://api.unsplash.com/photos/random/?client_id=b3e8bfaf42d7a4758419887d7947ce0be073819c632762a740329b03c6401554"
apiReq = requests.get(url, allow_redirects=True, timeout=10)

# print pulled image path
print(apiReq.json()['urls']['thumb'])

# check pulled value is a valid URL, using thumbnails as smaller
thumbLoc = apiReq.json()['urls']['thumb']
validThumb = "https://images.unsplash.com/photo" in thumbLoc

# if random image found and valid, download it and print to file.
if thumbLoc and validThumb :
  downloadReq = requests.get(thumbLoc, allow_redirects=True, timeout=10)
  open('randomImage.jpg', 'wb').write(downloadReq.content)

  # call the main hashing function from the hashImage file - returns a hashed version of the pulled image
  mainHash('randomImage.jpg', 'unsplash-salt')