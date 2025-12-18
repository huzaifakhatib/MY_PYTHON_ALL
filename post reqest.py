from pprint import pformat
import requests
r=requests.post("http://httpbin.org/post?a=b data={'harry':'value1'}")
print(r.text)