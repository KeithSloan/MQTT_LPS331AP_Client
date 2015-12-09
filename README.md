# MQTT_LPS331AP_Client
MQTT Client for LPS331AP sensor as in MikroElectronika Pressure Click

# Hardware Used
I went for the 2-way shield but there is a single shield availabe`
### Hardware used
* Raspberry Pi B+ ( But should work on 2B)
* [pi2-shield](http://www.mikroe.com/click/pi2-shield/)
* [pressure click](http://www.mikroe.com/click/pressure/)

I ordered mine from RS Components

### Alternative Hardware
* [Single pi shield](http://www.mikroe.com/click/pi-shield/)
* [Weather Click](http://www.mikroe.com/click/weather/)
(Would need different/altered software to read sensor)

### Install this software
From directory /home/pi issue command

**git clone https://github.com/KeithSloan/MQTT_LPS331AP_Client.git**

## Setting up I2C
I2C must be enabled on the Raspberry Pi - 
see [Setting up I2C](http://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi)

When you get to the testing stage i.e. Running 
**sudo i2cdetect -y 1**

You should see an I2C device at address 5d

Once you can see the I2C device at 5d you can check the sensor is working by running

**python /home/pi/MQTT_LPS331AP_Client/ReadSensor.py**

For MQTT you need to install mosquitto which can be done by following the [instructions](http://mosquitto.org/2013/01/mosquitto-debian-repository/)

The client uses Paho, a Python MQTT client library.

Begin by installing the latest version of Paho on the Pi:

*sudo pip-3.2 install paho-mqtt*

Before running the clint it is suggested that you edit mqtt_client.py

and change the values at the start of file to your requirements
1.host
2.queue
3.interval

to run the client

python mqtt_client.py

### Testing with node-red

The following json can be pasted into Node-red for simple testing

...json
[{"id":"b0402dd5.87c808","type":"mqtt-broker","z":"59eed34b.dc0c04","broker":"localhost","port":"1883","clientid":"","usetls":false,"verifyservercert":true,"compatmode":true,"keepalive":"15","cleansession":true,"willTopic":"","willQos":"0","willRetain":null,"willPayload":"","birthTopic":"","birthQos":"0","birthRetain":null,"birthPayload":""},{"id":"265015c6.dd75da","type":"mqtt in","z":"59eed34b.dc0c04","name":"Sensor Queue","topic":"pi-one/sensor","broker":"b0402dd5.87c808","x":89,"y":419,"wires":[["d19ef67d.535c3"]]},{"id":"d19ef67d.535c3","type":"debug","z":"59eed34b.dc0c04","name":"","active":true,"console":"false","complete":"payload","x":349,"y":445,"wires":[]}]
...
