from socket import * 
from string import * 

# Create socket and bind to address 
UDPSock = socket(AF_INET,SOCK_DGRAM) 
UDPSock.bind(("",1964)) 

# Receive messages 
while True: 
  data,addr = UDPSock.recvfrom(1964) 
  data = str(data,'utf-8')
  if data=='q': 
    print("Program has exited!")
    break 
  else: 
    print(data,addr[0])

# Close socket 
UDPSock.close() 
