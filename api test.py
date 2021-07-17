import requests

req = requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=326f27618c35752b70bcd50907c3b95d&user_id=193454650%40N05&format=json&nojsoncallback=1")
code = req.status_code
assert code==200 , "code doesnt match"
print(req.json())
print(req.headers)
print(req.content)
print(req)
