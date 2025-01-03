from pydoc import cli
import paho.mqtt .client as mqtt

def connect_result(client,userdata,flags,rc):
    print("connect..."+str(rc))
    if rc == 0:
        client.subscribe("test/#")
    else:
        print("연결실패")

def on_message(client, userdata, message):
    myval = message.payload
    print(myval)
    #print(type(myval))

try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message

    #bloker에 접속하기
    mqttClient.connect("192.168.0.71",1883,60)
    mqttClient.loop_forever()

except KeyboardInterrupt:
    pass
