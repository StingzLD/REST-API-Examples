"""
How do I Send a GET Request with Bearer Token Authorization Header?

To send a GET request with a Bearer Token authorization header, you need to
make an HTTP GET request and provide your Bearer Token with the Authorization:
Bearer {token} HTTP header. Bearer Authentication (also called token
authentication) is an HTTP authentication scheme created as part of OAuth 2.0
but is now used on its own. For security reasons, bearer tokens are only sent
over HTTPS (SSL). Click Send to run the GET request with a bearer token
authorization header example online and see results.
"""
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/get/json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {token}"


resp = requests.get(url, headers=headers)

print(resp.status_code)
