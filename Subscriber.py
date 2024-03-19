"""
This script demonstrates a MQTT subscriber that connects to a broker and subscribes to specific topics.
It uses the Paho MQTT client library to establish the MQTT connection and handle incoming messages.
This code announces the subscriber's status and subscribes to two topics: "messages/general" and "device/{subscriber_id}".
"""

import paho.mqtt.client as mqtt  # Import the Paho MQTT client
import time  # Import the time module

# Define the MQTT broker settings
broker = "localhost"  # broker ip address
port = 1883

subscriber_id = "device1"
status_topic = f"status/{subscriber_id}"
general_topic = "messages/general"
direct_topic = f"device/{subscriber_id}"

# Define the messages
lwt_message = "offline due to error"
offline_message = "offline"


# Define the callback function for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print(f"Connected with result code {rc}")
    client.publish(
        status_topic, "online", retain=True, qos=1
    )  # Publish an "online" message
    client.subscribe([(general_topic, 0), (direct_topic, 0)])  # Subscribe to the topics


# Define the callback function for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    print(
        f"Received on {msg.topic}: {msg.payload.decode()}"
    )  # Print out the received message


# Define the callback function for handling disconnection events
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(
            "Unexpected disconnection."
        )  # Print out a message if the disconnection was unexpected


# Setup the MQTT client and assign the callback functions
client = mqtt.Client()
client.will_set(
    status_topic, payload=lwt_message, qos=1, retain=True
)  # Set the Last Will and Testament (LWT) of the client
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the MQTT broker
try:
    client.connect(broker, port, 60)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Start the network loop in a non-blocking way
client.loop_start()

try:
    input("Press Enter to disconnect...\n")
finally:
    client.publish(
        status_topic, offline_message, retain=True
    )  # Publish an "offline" message
    time.sleep(1)  # Wait to ensure the "offline" message is sent before disconnecting
    client.disconnect()  # Disconnect from the broker
    client.loop_stop()  # Stop the network loop
