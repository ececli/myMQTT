# Use MQTT for Raspberry Pi

The purpose of this code is to wirelessly transfer data from one Raspberry Pi to another Raspberry Pi. All Raspberry Pi's must be in one network. The transmitter needs to know the IP address of the receiver. 

Actually, to achieve this goal, one simple method is to use `socket`. I tried it based on the tutorial online. The [Sender](Socket_Example/sendData_socket.py) and [Receiver](Socket_Example/recvData_socket.py) codes are also put under this topic. 

I chose to use MQTT since it could be easily expanded to multiple devices. 

## My Understanding of MQTT

In a MQTT system, there must be a server, which is called a broker, and at least one client. The clients can send data to the broker and read data from the broker. The IP address of the broker must be known by each client. Note that one Raspberry Pi can act as both broker and client. 

For a client to receive data, this client must firstly connect to the broker and subscribe the topic. Then, any data under this topic will be received by this client. A client can subscribe multiple topics at the same time. Here I used the simplest mode, which the client cannot receive the data before it subscribes the topic. 

The sender part is easy. The sender needs to first connect to the broker. Then it can publish (i.e., send) data under a certain topic to the broker. The data can be a string, byte-array, int, or float value.  



## Install, Setup and Operate MQTT

### Install and Activate MQTT Broker (Server)

To install an MQTT broker, use the following command:
> sudo apt install mosquitto mosquitto-clients

After installing it, it will be automatically `active`. But to make sure it will be `active` after the system reboots, the following command is needed: 
> sudo systemctl enable mosquitto
> 
To check the status of the MQTT service, run the following command: 
> systemctl status mosquitto

### Install MQTT Python Library

To install the MQTT library for Python, run the following command: 
> sudo pip3 install paho-mqtt

### Operate MQTT in Python

In short, there are several easy steps to use MQTT in Python. 
1. Connect to the broker; 
2. Subscribe the topic;
3. Setup receiver;
4. Publish a message;
5. Disconnect from the broker.

And each step has its callback function. 

Specifically, to use MQTT, we need to import the MQTT library:
> import paho.mqtt.client as mqtt

and then create an instance:
> client = mqtt.Client(client_name)

If `client_name` (string) is not provided, the system will generate a client name. 

Then, by following the above steps, we can handle it easily. I am skipping the details of each step. The detailed tutorial can be found [here](http://www.steves-internet-guide.com/mqtt-python-beginners-course/).


## Use myMQTT_Class.py to Send and Receive Data

Based on my needs, I wrote a class ([myMQTT](myMQTT_Class.py)) to use the MQTT. To use `myMQTT`, first create an instance: 
> client = myMQTT(broker_address, client_name)

If `client_name` is not provided, the system will generate one. Once the instance is created, the system will connect to the broker and print "Connected Successfully" if the broker is connected. 

Once it is connected to the broker, if the Raspberry Pi needs to send the data out, simply write:
> client.sendMsg(topic, data)

Note that `data` can be an integer array or just one integer. Note that currently, only integer can be sent, as is required by my project. I may expand to support float number or string in future. 


On the receiver side, once the instance `client` is generated, the client needs first to subscribe the topic, by
> client.registerTopic(topic)

Once the client subscribe the topic, it will then automatically receive data under this topic. But to read the data, this code is needed:
> data = client.readTopicData(topic)

Inside the class, a queue is used to store the data. Thus, when `client.readTopicData(topic)` is executed, the data is pull from the queue, which means you cannot get the data again if you do `client.readTopicData(topic)` one more time. It will only give you the data newly received. 

Therefore, one may want to know the length of data received before pull the data out. To do so, use this code:
> length = client.checkTopicDataLength(topic)


Two example files are put under this topic. One is for [sending the data](sendData_myMQTT.py) while the other one is for [receiving the data](recvData_myMQTT.py). 

---
Here are two useful links I used to learn MQTT. One is [MQTT for Python](http://www.steves-internet-guide.com/mqtt-python-beginners-course/), while the other one is [Build An MQTT Server](https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi). 
