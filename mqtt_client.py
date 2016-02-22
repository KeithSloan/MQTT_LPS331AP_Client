import paho.mqtt.client as paho
import smbus
import csv
import time, os

#host="messagesight.demos.ibm.com"
host="pi-one.local"
port=1883
queue="pi-one/sensor"
interval=60
#Init bus
bus = smbus.SMBus(1)

def InitSensor():
    # power up LPS331AP pressure sensor & set BDU bit
    bus.write_byte_data(0x5d, 0x20, 0b10000100)

def GetTemperature() :
    Temp_LSB = bus.read_byte_data(0x5d, 0x2b)
    Temp_MSB = bus.read_byte_data(0x5d, 0x2c)
    
    #combine LSB & MSB
    count = (Temp_MSB << 8) | Temp_LSB
     
    # As value is negative convert 2's complement to decimal
    comp = count - (1 << 16)

    #calc temp according to data sheet
    return(round(42.5 + (comp/480.0),2))

def GetPressure() :
    Pressure_XLB = bus.read_byte_data(0x5d, 0x28)
    Pressure_LSB = bus.read_byte_data(0x5d, 0x29)
    Pressure_MSB = bus.read_byte_data(0x5d, 0x2a)

    count = (Pressure_MSB << 16) | ( Pressure_LSB << 8 ) | Pressure_XLB
    #comp = count - (1 << 24)
    #Pressure value is positive so just use value as decimal 
    
    return(round(count/4096.0,2))


def ReadValuesPublish():
    #option to do a single read
    #write value 0b1 to register 0x21 on device at address 0x5d
    bus.write_byte_data(0x5d,0x21, 0b1)
    temperature = str(GetTemperature())
    print "Temperature : " + temperature
    pressure    = str(GetPressure())
    print "Pressure    : " + pressure
    msg = temperature+", "+pressure 
    client.publish(queue,msg)

def on_connect(pahoClient, obj, rc):
# Once connected, publish message
    print "Connected Code = %d"%(rc)
#        client.publish("prueba/123", "Hello World", 0)


def on_log(pahoClient, obj, level, string):
    print string

def on_publish(pahoClient, packet, mid):
# Once published, disconnect
    print "Published"
#    pahoClient.disconnect()

def on_disconnect(pahoClient, obj, rc):
        print "Disconnected"

# Initialise Sensor
InitSensor()
# Create a client instance
client=paho.Client()

# Register callbacks
client.on_connect = on_connect
client.on_log = on_log
client.on_publish = on_publish
client.on_disconnnect = on_disconnect

#Set userid and password
#client.username_pw_set(userID, password)

#connect
x = client.connect(host, port, 60)
client.loop_start()
try :
   while True :
         ReadValuesPublish()
         time.sleep(interval)
except KeyboardInterrupt:
   print("Interrupted")
   client.loop_stop()
