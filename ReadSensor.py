import smbus

#init bus
bus = smbus.SMBus(1)

# power up LPS331AP pressure sensor
bus.write_byte_data(0x5d, 0x20, 0b10000000)

#write value 0b1 to register 0x21 on device at address 0x5d
bus.write_byte_data(0x5d,0x21, 0b1)

Temp_LSB = bus.read_byte_data(0x5d, 0x2b)
Temp_MSB = bus.read_byte_data(0x5d, 0x2c)

#combine LSB & MSB
count = (Temp_MSB << 8) | Temp_LSB

# As value is negative convert 2's complement to decimal
comp = count - (1 << 16)

#calc temp according to data sheet
Temp = 42.5 + (comp/480.0)

print "Temperature: %.2f" % Temp
#print "Temp MSB ",format(Temp_MSB,'02x')
#print "Temp LSB ",format(Temp_LSB,'02x')
#print "Temp 2 comp ",format(count,'04x')
#print "Temp : ",format(comp,'04x')
#print "Temp MSB dec : ",Temp_MSB
#print "Temp_LSB dec : ",Temp_LSB

Pressure_LSB = bus.read_byte_data(0x5d, 0x29)
Pressure_MSB = bus.read_byte_data(0x5d, 0x2a)
Pressure_XLB = bus.read_byte_data(0x5d, 0x28)

count = (Pressure_MSB << 16) | ( Pressure_LSB << 8 ) | Pressure_XLB
#comp = count - (1 << 24)
#Pressure value is positive so just use value as decimal 
Pressure = count/4096.0 

print "Pressure: %.2f" % Pressure
#print "Pressure MSB ",format(Pressure_MSB,'02x')
#print "Pressure LSB ",format(Pressure_LSB,'02x')
#print "Pressure XLB ",format(Pressure_XLB,'02x')
#print "Pressure 2 comp ",format(count,'06x')
#print "Pressure : ",format(comp,'04x')


