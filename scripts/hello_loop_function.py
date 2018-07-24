import time
def loop():
	while True:
		print "Hello World!"
		time.sleep(.25)

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Good bye'
