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
	def testSpi(self):
		spidev = file(self.spidevFile, "wb")
		leds = ledstrip.LEDStrip(self.numberOfPixels,spidev)
		self.assertTrue(leds.spi,"SPI interface could not be opened")

	##
	# testNumPixels	Tests if the number of pixels is set properly.
	def testNumPixels(self):
		#spidev = open(self.spidevFile, "wb")
		self.assertRaises(IOError, open, self.spidevFile, "wb")
		leds = ledstrip.LEDStrip(self.numberOfPixels,spidev)
		self.assertEqual(self.numberOfPixels,leds.numPixels(),"Number of pixels do not match")

if __name__ == "__main__":
	unittest.main()
