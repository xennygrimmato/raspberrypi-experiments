import unittest
import sys
sys.path.append("../")
from ledStrip import ledstrip

class TestLEDStrip(unittest.TestCase):

	##
	# setUp			Sets the initial values for number of leds and spidev file path.
	def setUp(self):
		self.numberOfPixels = 32
		self.spidevFile = "/dev/spidev0.0"
	
	##
	# testSpi		Tests if the SPI connection is working.
	def testConstructor(self):
		spidev = open(self.spidevFile, "wb") # spidev is the file object of the SPI connection
		leds = ledstrip.LEDStrip(self.numberOfPixels, spidev) # Initialise the constructor.

	##
	# testNumPixels	Tests if the number of pixels is set properly.
	def testNumPixels(self):
		spidev = open(self.spidevFile, "wb") # spidev is the file object of the SPI connection
		leds = ledstrip.LEDStrip(self.numberOfPixels,spidev) # Initialise the constructor.
		self.assertEqual(self.numberOfPixels,leds.numPixels(), "Number of pixels do not match") # assert equality of numberOfPixels and value returned by numPixels()

if __name__ == "__main__":
	unittest.main()
