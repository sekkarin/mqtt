import paho.mqtt.subscribe as subscribe


def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))


subscribe.callback(print_msg,"Data_Sensor/Temperature", hostname="test.mosquitto.org",port=1883,client_id='e0c06be3-5f7a-4566-8239-c737e1d95f39')
