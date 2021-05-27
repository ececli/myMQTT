from myMQTT_Class import myMQTT
import numpy as np

broker_address = "192.168.1.210"
topic1 = "ranging/delay/t3t2_delay_ms"
topic2 = "ranging/delay/t3t2_delay_count"
mqttc = myMQTT(broker_address) 

a = np.round(abs(np.random.randn(10))*1000000)
print(a)
b = np.round(abs(np.random.randn(10))*1000000)
print(b)

mqttc.sendMsg(topic1,a) # send data under a certain topic
mqttc.sendMsg(topic2,b)

