# Use MQTT for Raspberry Pi

The purpose of this code is to wirelessly transfer data from one Raspberry Pi to another Raspberry Pi. All Raspberry Pi's must be in one network. The transmitter needs to know the IP address of the receiver. 

Actually, to achieve this goal, one simple method is to use `socket`. I tried it based on the tutorial online. The [Sender](Socket_Example/sendData_socket.py) and [Receiver](Socket_Example/recvData_socket.py) codes are also put under this topic. 

I chose to use MQTT since it could be easily expanded to multiple devices. 

## My Understanding of MQTT

## Install and Setup MQTT

### Install MQTT Broker (Server)

To install an MQTT broker, use the following command:
> sudo apt install mosquitto mosquitto-clients

After installing it, it will be automatically `active`. But to make sure it will be `active` after reboot, the following command is needed: 
> sudo systemctl enable mosquitto
> 
To check the status of the MQTT service, run the following command: 
> systemctl status mosquitto

### Install MQTT Python Library

To install the MQTT library for Python, run the following command: 
> sudo pip3 install paho-mqtt


## Use myMQTT_Class.py to Send and Receive Data

---
Here are two useful links I used to learn MQTT. One is [MQTT for Python](http://www.steves-internet-guide.com/mqtt-python-beginners-course/), while the other one is [Build An MQTT Server](https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi). 
