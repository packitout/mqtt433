#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import paho.mqtt.client as mqtt
import logging
import subprocess

def on_connect(client, userdata, flags, rc):
    logging.info("CNNACK received with code %d." % (rc))

def on_publish(client, userdata, mid):
    logging.info("mid: "+str(mid))

logging.basicConfig(filename=__file__.replace(".py",'.log'),level=logging.INFO)
logging.info("start")

mqttc = mqtt.Client("python_pub")
mqttc.username_pw_set(username="<MQTTUSERNAME>", password="<MQTTPASSWORD>")
mqttc.connect("localhost", port=1883)
mqttc.loop_start()
logging.info("main loop")

proc = subprocess.Popen(['rtl_433', '-F', 'json', '-R', '11', '-R', '39'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    try:
        logging.debug("listening")
#        input = sys.stdin.readline()
        input = proc.stdout.readline()
        payload = json.loads(input.decode("utf-8"))
        logging.debug(payload)
        (rc, mid) = mqttc.publish("hass/rtl_433/sensor_" + str(payload['id']) , json.dumps(payload))
#        (rc, mid) = mqttc.publish("hass/rtl_433", json.dumps(payload))
        logging.debug("rc=%s, mid=%s" % (rc, mid))
        mqttc.loop(2) # timeout = 2s
        logging.debug("published")
    except Exception as x:
        logging.warning("exception %s" % x)
        logging.warning("input:'%s'" % input)
    except KeyboardInterrupt:
        sys.stdout.flush()
        logging.warning("exit")
        break
