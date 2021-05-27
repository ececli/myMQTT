# Use MQTT for Raspberry Pi

The purpose of this code is to wirelessly transfer data from one Raspberry Pi to another Raspberry Pi. All Raspberry Pi's must be in one network. The transmitter needs to know the IP address of the receiver. 

Actually, to achieve this goal, one simple method is to use `socket`. 

I chose to use MQTT since it could be easily applied to multiple devices. 




---
Here are two useful links I used to learn MQTT. One is [MQTT for Python](http://www.steves-internet-guide.com/mqtt-python-beginners-course/), while the other one is [Build An MQTT Server](https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi). 
