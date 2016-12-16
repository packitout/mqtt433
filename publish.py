# -*- coding: utf-8 -*-
# script used to test the paho mqtt publishing in python
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
mqttc.username_pw_set(username="<MQTTUSERNAME>", password="<MQTTPASSWORD>")
mqttc.connect("localhost", port=1883)


payload = { "time" : "2016-10-06 15:17:13", 
            "model" : "Fine Offset Electronics, WH2 Temperature/Humidity sensor", 
            "id" : 125, 
            "temperature_C" : 28.300, 
            "humidity" : 43}

mqttc.publish("hass/sensor", str(payload))
mqttc.loop(2) # timeout = 2s
