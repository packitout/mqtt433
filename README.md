# mqtt433
mqtt433 python service script to use rtl_433 and a SDR dongle to read Acurite temperature/humidity sensors (or other 433MHz) into JSON and publish to MQTT topic for Homeassistant sensor integration. I did not write the originals of these scripts, merely debugged for my own purposes.

PS I am NOT a coding or networking expert. Merely a hobbist so please do your own diligence on security and excuse any sloppy programming. Thanks!

## mqtt433.py
this is the python script to run as a service. it requires paho-mqtt (https://pypi.python.org/pypi/paho-mqtt/1.1). Right now it only uses user authentication for the MQTT broker (so put the username and password you want this system to use to connect to the broker into this code) since it is meant to run on the hub machine connecting to the broker with the 1833 port (as opposed to the 8833 port for TLS encrypted traffic of MQTT clients outside the local network).

the line that defines "proc" specifies the rtl_433 call in the subprocess. In this example, the rtl_433 options are to output in JSON and only look for the two types of Acurite sensors I implemented. Use rtl_433 --help in the shell for more information.

It publishes to the topic "hass/rtl_433/sensor_0000" where 0000 is the sensor id number. This means you are not limited to the ABC channels on the Acurite tower sensors. They will have different id numbers so you can tell them apart. An easy way to find the id number is to either run rtl_433 in the shell to sniff their signals or use the commented line in mqtt433.py to publish any sensor output to the 'hass/rtl_433" MQTT topic and listen to that topic. Nice for debugging JSON outputs too.

## listener.py and publish.py
just used to listen or publish to MQTT topics for debugging.
