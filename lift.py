import Adafruit_BBIO.GPIO as GPIO
import time
import thread

GPIO.setup("P8_10", GPIO.IN)
GPIO.setup("P8_12", GPIO.IN)
GPIO.setup("P8_14", GPIO.IN)

GPIO.setup("P8_18", GPIO.OUT)        # Level 1
GPIO.setup("P8_20", GPIO.OUT)        # Level 2
GPIO.setup("P8_22", GPIO.OUT)        # Level 3

present_level = 1
old_switch_state = 0

GPIO.output("P8_18", GPIO.HIGH)      # Initially at Level 1.

del level_1():
	if(present_level == 1):
		GPIO.output("P8_18", GPIO.HIGH)
	else if(present_level == 2):
		GPIO.output("P8_20", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_18", GPIO.HIGH)
	else if(present_level == 3):
		GPIO.output("P8_22", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_20", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_18", GPIO.HIGH)

	present_level = 1

del level_2():
	if(present_level == 1):
		GPIO.output("P8_18", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_20", GPIO.HIGH)
	else if(present_level == 2):
		GPIO.output("P8_20", GPIO.HIGH)
	else if(present_level == 3):
		GPIO.output("P8_22", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_20", GPIO.HIGH)

	present_level = 2

del level_3():
	if(present_level == 1):
		GPIO.output("P8_18", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_20", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_22", GPIO.HIGH)
	else if(present_level == 2):
		GPIO.output("P8_20", GPIO.HIGH)
		time.sleep(1)
		GPIO.output("P8_22", GPIO.HIGH)
	else if(present_level == 3):
		GPIO.output("P8_22", GPIO.HIGH)

	present_level = 3

def get_requests():
	while True:
		new_switch_state_1 = GPIO.input("P8_10")
		new_switch_state_2 = GPIO.input("P8_12")
		new_switch_state_3 = GPIO.input("P8_14")


def take_action():
	if new_switch_state_1 == 1:        
		level_1()
	
	if new_switch_state_2 == 1:        
		level_2()

	if new_switch_state_3 == 1:        
		level_3()

try:
   thread.start_new_thread(get_requests)
   thread.start_new_thread(take_action)
except:
   print "Error."
