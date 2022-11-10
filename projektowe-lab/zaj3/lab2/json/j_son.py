import requests
import json # mniej ważący format od xml poniewaz nie ma znacznikow 
site = "https://danepubliczne.imgw.pl/api/data/synop/id/12566"

r = requests.get(site)

print(r.text)

d = json.loads(r.text)

print(d)

for k in d:
  print(k,d[k])



