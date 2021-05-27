from myMQTT_Class import myMQTT


broker_address="192.168.1.210" # broker address
topic1 = "ranging/delay/t3t2_delay_ms"
topic2 = "ranging/delay/t3t2_delay_count"
mqttc = myMQTT(broker_address, "RPi2") 
mqttc.registerTopic(topic1) # subscribe the topic so that it could receive data for this topic
mqttc.registerTopic(topic2)


while True:
    # stop when the amount of data is satisfied
    # The sender sends 10 int values for each topic
    if mqttc.checkTopicDataLength(topic1)==10 and mqttc.checkTopicDataLength(topic2)==10: 
        mqttc.closeClient()
        break

# export the data to the local variables
a = mqttc.readTopicData(topic1)
b = mqttc.readTopicData(topic2)
print(a)
print(b)
