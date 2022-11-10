import requests
import xmltodict
import time

r = requests.get("http://meteo2.ftj.agh.edu.pl/meteo/meteo.xml")

print(r.text)

dic = xmltodict.parse(r.text)['meteo']['dane_aktualne']

for k in dic:
  print(k,dic[k].split()[0])

#print(time.ctime(),dic['meteo']['dane_aktualne']['sx'])

  