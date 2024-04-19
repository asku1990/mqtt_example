# This code is a simple MQTT publisher that connects to a local MQTT broker,
# publishes messages to two topics, and subscribes to all topics of interest.
# You can use this code to test the MQTT broker and the subscriber code.


# Import the necessary libraries
import paho.mqtt.client as mqtt
import time

# Define the MQTT broker and port
broker = "192.168.50.53"  # broker ip address
port = 1883  # Define the port to use for the connection


# This function is called when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully.")
        # Subscribe to all topics of interest upon connecting
        client.subscribe("status/#")
    else:
        print(f"Failed to connect, return code {rc}")


# This function is called when a message is received from the MQTT broker
def on_message(client, userdata, msg):
    print(f"Received message on {msg.topic}: {msg.payload.decode()}")


# This function publishes messages to the MQTT broker
def publish_messages(client):
    # Define the topics and messages to be published
    topics = {
        "device/device1": "Hello device1",  # Publish a message to the "device/device1" topic when connected
        "device/device_umqtt": "Hello device_umqtt",  # Publish a message to the "device/device2" topic when connected
    }

    # Publish each message to its corresponding topic
    for topic, message in topics.items():
        client.publish(topic, message)
        print(f"Published to {topic}: {message}")


# The main function
def main():

    # Create a new MQTT client
    client = mqtt.Client()
    # Assign the functions to handle connect and message events
    client.on_connect = on_connect
    client.on_message = on_message

    # Try to connect to the MQTT broker
    try:
        client.connect(broker, port, 60)  # Connect to the MQTT broker
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        return

    # Start the MQTT client loop
    client.loop_start()
    # Publish messages
    publish_messages(client)

    # Wait for the user to press Enter before disconnecting
    try:
        input("Press Enter to disconnect...\n")
    finally:
        # Stop the MQTT client loop and disconnect from the broker
        client.loop_stop()
        client.disconnect()


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
