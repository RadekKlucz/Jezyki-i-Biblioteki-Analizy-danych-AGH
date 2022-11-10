#!/usr/bin/python3
# -*- coding: utf-8 -*-

end = None

import paho.mqtt.client as mqtt

BROKER = "localhost"

# BROKER = "mqtt.lab.ii.agh.edu.pl"

################################################################################

def send(topic,payload):
  global client

  client.publish(topic,payload,retain=True) #publish
  # client.publish(topic,payload,retain=False) #publish
end

################################################################################

def on_message(client, userdata, message):

  topic = message.topic
  payload = str(message.payload.decode("utf-8"))

  print("rcv",topic,payload)
end

################################################################################


def init():
  global client

  # print("creating new instance")
  client = mqtt.Client("abc") #create new instance
  client.on_message=on_message #attach function to callback
  print("connecting to broker")
  client.connect(BROKER) #connect to broker
  client.loop_start() #start the loop
  client.subscribe([("ala/#",0),("ola/#",0)])

end

################################################################################

def loop():
  while True:
    x = input(">>")
    send("ula",x)
  end
end

################################################################################

init()
loop()

################################################################################
