# This script is executed when the pico boots up. It is used to connect the pico to a WiFi network.
# just add this file to the root of the pico and it will connect to the wifi network

# Import necessary modules
import network, utime, machine

# Replace the following with your WIFI Credentials
SSID = "dev"
SSID_PASSWORD = "-xVP3vEZcBunE9w"


# Function to connect to the WiFi
def do_connect():
    # Create an instance of the network.WLAN class for the station interface
    sta_if = network.WLAN(network.STA_IF)

    # Check if the station interface is not connected to a WiFi network
    if not sta_if.isconnected():
        print("connecting to network...")
        # Activate the station interface
        sta_if.active(True)
        # Connect to the WiFi network using the SSID and password
        sta_if.connect(SSID, SSID_PASSWORD)

        # Keep trying to connect to the WiFi network until a connection is established
        while not sta_if.isconnected():
            print("Attempting to connect....")
            # Wait for 1 second before trying to connect again
            utime.sleep(1)

    # Print a success message along with the network configuration
    print("Connected! Network config:", sta_if.ifconfig())


# Print a message indicating that the script is trying to connect to the WiFi network
print("Connecting to your wifi...")
# Call the do_connect function to connect to the WiFi network
do_connect()
