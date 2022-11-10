import requests
import json

site = "http://api.open-notify.org/iss-now.json"
res = requests.get(site)

print(res.text)

d = json.loads(res.text)

print(d)

print(d['message'])
print(d['timestamp'])
print(d['iss_position']['longitude'], d['iss_position']['latitude'])

# Example prints:
#   1364795862
#   -47.36999493 151.738540034
