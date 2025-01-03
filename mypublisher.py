import paho.mqtt.publish as publisher

publisher.single("test/topic","led_on",hostname="192.168.0.71")
