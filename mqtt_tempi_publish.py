import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

### Broker connection
mqttBroker ="mqtt.eclipseprojects.io"
### Client
client = mqtt.Client("Temperature_inside")
### client connects to Broker
client.connect(mqttBroker)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
