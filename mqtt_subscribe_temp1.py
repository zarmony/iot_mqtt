import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))


### Broker connection
mqttBroker ="mqtt.eclipseprojects.io"
### Client
client = mqtt.Client("Smartphone")
### client connects to Broker
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(300)
client.loop_stop()
