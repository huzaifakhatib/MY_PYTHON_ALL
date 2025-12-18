import requests
# Use PUT instead of GET
r = requests.put('http://httpbin.org/put', data={"a": 1, "b": 2})
print(r.text)
print(r.json())