import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

anodes = [11,12,13]
cathodes = [15,16,18]
sleeptime = 1.0
speed = 10


one = [[1,1,1], [1,0,1], [1,1,1]]
two = [[1,1,0], [1,1,1], [0,1,1]]
three = [[0,1,1], [1,0,1], [1,1,0]]
four = [[0,1,0], [1,1,1], [0,1,0]]
five = [0,1,0], [1,0,1], [0,1,0]
six = [[0,1,0], [0,1,0], [0,1,0]]

ani = [one, two, three, four, five, six]


def initLeds():
	for anode in anodes:
		GPIO.setup(anode, GPIO.OUT)
	for cathode in cathodes:
		GPIO.setup(cathode, GPIO.OUT)

def turnLedsOff():
	for anode in anodes:
		GPIO.output(anode, 0)
	for cathode in cathodes:
		GPIO.output(cathode, 0)

def testRows():		
	GPIO.output(anodes[0], 1)
	time.sleep(sleeptime/2)

	GPIO.output(anodes[0], 0)
	GPIO.output(anodes[1], 1)
	time.sleep(sleeptime/2)

	GPIO.output(anodes[1], 0)
	GPIO.output(anodes[2], 1)
	time.sleep(sleeptime/2)
	
def testColumns():
	GPIO.output(anodes[0], 1)
	GPIO.output(anodes[1], 1)
	GPIO.output(anodes[2], 1)
	GPIO.output(cathodes[1], 1)
	GPIO.output(cathodes[2], 1)
	time.sleep(sleeptime/2)

	GPIO.output(cathodes[0], 1)
	GPIO.output(cathodes[1], 0)
	time.sleep(sleeptime/2)

	GPIO.output(cathodes[1], 1)
	GPIO.output(cathodes[2], 0)
	time.sleep(sleeptime/2)

def testLeds():
	turnLedsOff()
	testRows()
	turnLedsOff()
	testColumns()
	turnLedsOff()

initLeds()
testLeds()

try:
	while True:
		for frame in range(6):
			for pause in range(speed):
				for i in range(3):
					GPIO.output(cathodes[0], ani[frame][i][0])
					GPIO.output(cathodes[1], ani[frame][i][1])
					GPIO.output(cathodes[2], ani[frame][i][2])
					
					GPIO.output(anodes[i], 1)
					time.sleep(sleeptime/100)
					GPIO.output(anodes[i], 0)
	
except KeyboardInterrupt:
	GPIO.cleanup()

