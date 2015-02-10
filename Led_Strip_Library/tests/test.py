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

	##
	# testColor		Tests if the color is returned correctly.
	def testColor(self):
		spidev = open(self.spidevFile, "wb") # spidev is the file object of the SPI connection
		leds = ledstrip.LEDStrip(self.numberOfPixels,spidev) # Initialise the constructor.
		
		# Assign 7 bit binary values to red, green and blue colors
		redColorValue = '1110010'
		greenColorValue = '0111000'
		blueColorValue = '0000011'
		
		colorValue = bin(leds.color(int(redColorValue,2),int(blueColorValue,2),int(greenColorValue,2)))[2:]

		# Check if returned colorValue matched the set colors
		self.assertEqual(colorValue[0:8],"1"+redColorValue,"Red color does not match")
		self.assertEqual(colorValue[16:24],"1"+greenColorValue,"Green color does not match")
		self.assertEqual(colorValue[8:16],"1"+blueColorValue,"Blue color does not match")

if __name__ == "__main__":
	unittest.main()
