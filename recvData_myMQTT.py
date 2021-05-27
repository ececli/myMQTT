from myMQTT_Class import myMQTT


broker_address="192.168.1.210"
topic1 = "ranging/delay/t3t2_delay_ms"
topic2 = "ranging/delay/t3t2_delay_count"
mqttc = myMQTT(broker_address, "RPi2")
mqttc.registerTopic(topic1)
mqttc.registerTopic(topic2)


while True:
    if mqttc.checkTopicDataLength(topic1)==10 and mqttc.checkTopicDataLength(topic2)==10:
        mqttc.closeClient()
        break


a = mqttc.readTopicData(topic1)
b = mqttc.readTopicData(topic2)
print(a)
print(b)
