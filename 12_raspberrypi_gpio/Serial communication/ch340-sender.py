import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

counter=0

while 1: 
	# Convert the Unicode string to bytes
	message = f'Write counter: {counter} \n'
	encoded_message = message.encode()
	ser.write(encoded_message)
	time.sleep(1) 
	counter += 1
