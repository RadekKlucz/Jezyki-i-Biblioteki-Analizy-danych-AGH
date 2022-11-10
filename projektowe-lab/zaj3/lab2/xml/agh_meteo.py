import socket

import xmltodict

import time


while True:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(('meteo2.ftj.agh.edu.pl',80))
  sock.send(b"GET /meteo/meteo.xml\n")
  s = sock.recv(1024).decode()
  sock.close()


  # print(s)
  # print()

  dic = xmltodict.parse(s)
  print(time.ctime(),dic['meteo']['dane_aktualne']['sx'])
  time.sleep(60)

  