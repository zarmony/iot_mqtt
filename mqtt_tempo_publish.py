import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

### Broker connection
mqttBroker ="mqtt.eclipseprojects.io"
### Client
client = mqtt.Client("Temperature_Outside")
### client connects to Broker
client.connect(mqttBroker)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
