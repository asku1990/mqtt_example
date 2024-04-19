# thia script is a simple MQTT subscriber that connects to a broker and subscribes to a topic.
# you need to have an MQTT broker running on your network to test this script.
# you need to add umqtt.simple library to your pico with thonny

import time
import ubinascii
from umqtt.simple import MQTTClient
import machine

# Default MQTT server to connect to (change if needed)
MQTT_BROKER = "192.168.50.53"
# Unique client ID for the MQTT client
CLIENT_ID = b"device_umqtt"
# Topics to subscribe to
DIRECT_TOPIC = b"device/device_umqtt"
# Topic to publish status messages to
STATUS_TOPIC = b"status/device_umqtt"

# Message to publish when the client goes offline
OFFLINE_MESSAGE = b"offline"


# Callback function to handle received messages
# This function is called whenever a message is received on a subscribed topic
def sub_cb(topic, msg):
    # Print the topic and message
    print((topic, msg))


# Function to handle actions after connecting to the MQTT broker
def on_connect(mqttClient):
    # Print a success message
    print("Connected successfully.")
    # Publish an "online" message to the status topic
    mqttClient.publish(STATUS_TOPIC, b"online", retain=True, qos=1)
    # Subscribe to the general and direct topics
    mqttClient.subscribe(DIRECT_TOPIC)


# Function to handle actions before disconnecting from the MQTT broker
def on_disconnect(mqttClient):
    # Publish an "offline" message to the status topic
    mqttClient.publish(STATUS_TOPIC, OFFLINE_MESSAGE, retain=True)
    # Disconnect from the broker
    mqttClient.disconnect()


# Main function
def main():
    # Print a message indicating that the client is attempting to connect to the broker
    print(f"Begin connection with MQTT Broker :: {MQTT_BROKER}")
    # Create a new MQTT client
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER)
    # Set the callback function to handle received messages
    mqttClient.set_callback(sub_cb)
    # Connect to the broker
    mqttClient.connect(clean_session=True)

    # Call the on_connect function
    on_connect(mqttClient)

    # Print a message indicating that the client is waiting for messages
    print(
        f"Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!"
    )

    # Main loop
    try:
        while True:
            # Check for new messages
            mqttClient.check_msg()
            # Sleep for 1 second
            time.sleep(1)
    # If the user presses Ctrl+C, call the on_disconnect function
    except KeyboardInterrupt:
        on_disconnect(mqttClient)


# If this script is the main script, call the main function
if __name__ == "__main__":
    main()
