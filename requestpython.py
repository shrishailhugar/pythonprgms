import requests
from pprint import pprint
import json
# from urllib import request
import os

response=requests.get("http://216.10.245.166/Library/GetBook.php",params={'AuthorName':'Rahul Shetty2'})
# print(response.text)

print(type(response))
status_code=response.status_code
print(response.status_code)

pprint(response.json(), indent=4)
print(response.headers)
# it will be a 
print(type(response.headers))

assert response.headers['Content-type']=='application/json;charset=UTF-8'
