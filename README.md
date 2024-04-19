# Python MQTT Publisher and Subscriber

This repository contains two Python scripts demonstrating the basic operations of MQTT (Message Queuing Telemetry Transport) publishers and subscribers using the Paho MQTT client library.

## Overview

### Introduction to MQTT

[MQTT](https://mqtt.org) stands for Message Queuing Telemetry Transport. This lightweight messaging protocol is optimized for low-bandwidth, low-footprint communication, making it perfect for connecting remote devices in the Internet of Things (IoT).

### Quality of Service (QoS) Levels

MQTT offers three levels of Quality of Service (QoS) to cater to different message delivery guarantees:

- **QoS 0 (At most once)**: Fast and lightweight, with no guarantee of delivery.
- **QoS 1 (At least once)**: Ensures delivery but may result in duplicate messages.
- **QoS 2 (Exactly once)**: Provides a guarantee of single, exact delivery, ideal for critical messages.

## Installation

To use these scripts, the Paho MQTT client library must be installed:

```
pip install -r requirements.txt
```

## Usage

Ensure you have a running MQTT broker (either a local instance or a remote service). Modify the `broker` and `port` variables in the scripts if needed to match your broker's settings. Run the scripts with Python 3:

```
python3 publisher.py
python3 subscriber.py
```

## Setting Up Your MQTT Broker

You need one broker running. All the devices need the same IP address for it.

### Broker Installation

For local testing, Mosquitto is a widely used MQTT broker. Installation varies by platform:

- **macOS**:
  ```
  brew install mosquitto
  ```
- **Linux**:
  ```
  sudo apt-get install mosquitto
  ```
- **Windows**: Download the installer from the [Eclipse Mosquitto website](https://mosquitto.org/download/).

### Starting the Broker

After installing, you may need to start the Mosquitto service manually, depending on your system's setup:

- **macOS** and **Linux**:
  ```
  brew services start mosquitto
  ```
  or
  ```
  sudo systemctl start mosquitto
  ```
- **Windows**: The Mosquitto service should start automatically after installation. If not, you can start it through the Services application.

### Broker Configuration

Edit the `mosquitto.conf` file to configure your broker. This file's location can vary:

- **macOS** (Homebrew installation): `/usr/local/etc/mosquitto/mosquitto.conf`
- **Linux**: `/etc/mosquitto/mosquitto.conf`
- **Windows**: `C:\Program Files\mosquitto\mosquitto.conf`

Add the following lines to enable basic communication and logging:

```
listener 1883
allow_anonymous true
log_type all
```

These commands set up the broker to listen on port 1883, allow anonymous connections, and log detailed information about its operation, aiding in development and troubleshooting. Please take a note that for beter security it is recommended use ip adress next to listener.

### Applying Configuration Changes

To apply your configuration changes, restart the Mosquitto service:

- **macOS** and **Linux**:
  ```
  brew services restart mosquitto
  ```
  or
  ```
  sudo systemctl restart mosquitto
  ```
- **Windows**: Restart the service through the Services application or by restarting your computer.

### Verifying Your Setup

To ensure your broker is running correctly, you can use the command-line utilities that come with Mosquitto:

- To subscribe to a topic:
  ```
  mosquitto_sub -h localhost -t test/topic
  ```
- To publish a message:
  ```
  mosquitto_pub -h localhost -t test/topic -m "Hello MQTT"
  ```

If everything is configured correctly, the subscriber should receive the "Hello MQTT" message shortly after it's published.

# Detailed Script Information

## publisher.py

This script is a simple MQTT publisher that connects to a local MQTT broker, publishes messages to two topics, and subscribes to all topics of interest. It's designed to test the MQTT broker and subscriber code interactions.

### Key Functions

- `on_connect`: Triggered upon client connection to the MQTT broker, subscribing to all topics of interest.
- `on_message`: Invoked when a message is received, displaying its content.
- `publish_messages`: Handles publishing messages to specified topics on the broker.

### Main Function

The `main` function orchestrates the connection to the MQTT broker, initiating message publishing, and managing user input to disconnect gracefully. It sets up the MQTT client, connects to the broker, and enters a loop to maintain the connection until the user decides to disconnect.

## subscriber.py

This script acts as an MQTT subscriber, establishing a connection to a broker and listening to messages on specified topics. It showcases how to use the Paho MQTT client to manage subscriptions and process incoming messages.

### Key Functions

- `on_connect`: Called after the server responds to the connection request. It publishes an "online" status message and sets up subscriptions to specific topics.
- `on_message`: Executed when a message arrives, printing its details.
- `on_disconnect`: Handles unexpected disconnection events, logging them for troubleshooting.

### Main Function

In `subscriber.py`, the `main` function is responsible for setting up the MQTT client, including configuring the Last Will and Testament (LWT) for notifying others in case of disconnection. It connects to the MQTT broker and starts a loop to keep the client running, allowing it to receive messages. User input triggers a clean disconnection process, ensuring the client's status is updated to "offline" before shutting down.

# Python umqtt.simple and umqtt_Subscriber

## Overview

This Python script demonstrates the basic operations of umqtt.simple, a Message Queuing Telemetry Transport (MQTT) library.

## Introduction to umqtt.simple

umqtt.simple is a library for MicroPython. It is lighter than the standard mqtt-paho library, making it suitable for devices with limited resources.

## Installation via Thonny

1. Start by pressing the pico BOOTSEL button and connecting your device to the computer using a micro USB cable.
2. Download the Raspberry Pi Pico Python SDK and transfer it to your Pico (which should appear as an external drive). You can find the SDK here: https://projects.raspberrypi.org/en/projects/get-started-pico-w/1
3. Install Pico Zero for handling electronic components (also available in the link provided).
4. Install umqtt.simple for MQTT connections.
5. The instructions also include a WLAN code that you can use to test the connection. (You can use boot.py also for testing)

## Connect to WLAN

Add the boot.py file to the root folder of the Pico so it will connect to the WLAN when it boots up. You can do this via Thonny:

1. Open the boot.py file.
2. Select File > Save Copy, then save to the Pico's root directory as boot.py.

You can test the code by just running the code.

NOTE: Remember to edit your WLAN SSID and password in the boot.py file.

## Connect to MQTT Broker

Ensure that the MQTT broker is running and note its IP address.
Edit the broker IP address in the umqtt_subscriber's code and run the code.
When you run the MQTT publisher, you should see status messages. The publisher will also send a "hello" message when it connects.

# Detailed Script Information

## boot.py

This script is a simple micropython code who connects to wlan.

## umqtt_subscriber.py

This script acts as an UMQTT.SIMPLE subscriber, establishing a connection to a broker and listening to messages on specified topics. It showcases how to use the umqtt.simpple client to manage subscriptions and process incoming messages.

### Key Functions

- `on_connect`: Called after the server responds to the connection request. It publishes an "online" status message and sets up subscriptions to specific topics.
- `sub_scb`: Executed when a message arrives, printing its details. (this is special function for umqtt.simple)
- `on_disconnect`: Handles unexpected disconnection events, logging them for troubleshooting.

### Main Function

In `umqtt_subscriber.py`, the `main` function is responsible for setting up the MQTT client, and notifying others in case of disconnection. It connects to the MQTT broker and starts a loop to keep the client running, allowing it to receive messages.

## Here's how to use Pico with VS Code:

1. Install the VS Code extension named MicroPico.
2. Select the command MicroPico: Connect. On a Mac, you can do this by pressing Shift + Cmd + P and typing the beginning of the command.
3. Next, select Configure Project from the same menu.
4. Now you can write your Python code and run it. I used the Play and Stop buttons from the status bar at the bottom.
