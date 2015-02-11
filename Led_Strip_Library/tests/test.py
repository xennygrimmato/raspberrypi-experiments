import unittest
import sys
sys.path.append("../")
from ledStrip import ledstrip

class TestLEDStrip(unittest.TestCase):

	##
	# setUp					Sets the initial values for number of leds and spidev file path.
	def setUp(self):
		self.numberOfPixels = 32
		self.spidevFile = "/dev/spidev0.0"
		self.spidev = open(self.spidevFile, "wb") # spidev is the file object of the SPI connection
		self.leds = ledstrip.LEDStrip(self.numberOfPixels, self.spidev) # Initialise the constructor.

	
	##
	# testNumPixels			Tests if the number of pixels is set properly.
	def testNumPixels(self):
		self.assertEqual(self.numberOfPixels,self.leds.numPixels(), "Number of pixels do not match") # assert equality of numberOfPixels and value returned by numPixels()

	##
	# testColor				Tests if the color is returned correctly.
	def testColor(self):
		
		# Assign 7 bit binary values to red, green and blue colors
		redColorValue = 114
		greenColorValue = 56
		blueColorValue = 3
		
		colorValue = bin(self.leds.color(redColorValue,blueColorValue,greenColorValue))[2:]

		# Check if returned colorValue matched the set colors
		self.assertEqual(int(colorValue[0:8],2)-128,redColorValue,"Red color does not match in testColor")
		self.assertEqual(int(colorValue[16:24],2)-128,greenColorValue,"Green color does not match in testColor")
		self.assertEqual(int(colorValue[8:16],2)-128,blueColorValue,"Blue color does not match in testColor")

	##
	# testUpdateLength		Tests updateLength function
	def testUpdateLength(self):

		# Change the number of pixels and test
		self.numberOfPixels = 40
		self.leds.updateLength(self.numberOfPixels)
		self.assertEqual(self.numberOfPixels,self.leds.numPixels(),"updateLength failed")

	##
	# testPixelColorRGB		Tests setPixelColorRGB and getPixelColorRGB
	def testPixelColorRGB(self):
		pixelValue = 3
		redColorValue = 34
		greenColorValue = 122
		blueColorValue = 78
		
		self.leds.setPixelColorRGB(pixelValue,redColorValue,greenColorValue,blueColorValue)
		
		self.assertEqual(self.leds.getPixelColorRGB(pixelValue)[1]-128, redColorValue, "Red color does not match in testPixelColorRGB")
		self.assertEqual(self.leds.getPixelColorRGB(pixelValue)[0]-128, greenColorValue, "Green color does not match in testPixelColorRGB")
		self.assertEqual(self.leds.getPixelColorRGB(pixelValue)[2]-128, blueColorValue, "Blue color does not match in testPixelColorRGB")
	

	##
	# testPixelColor		Tests setPixelColor and getPixelColor
	def testPixelColor(self):
		pixelValue = 10
		redColorValue = 34
		greenColorValue = 122
		blueColorValue = 78
		
		self.leds.setPixelColor(pixelValue,self.leds.color(redColorValue,greenColorValue,blueColorValue))

		colorValue = bin(self.leds.getPixelColor(pixelValue))[2:]
		self.assertEqual(int(colorValue[8:16],2)-128, redColorValue, "Red color does not match in testPixelColor")
		self.assertEqual(int(colorValue[0:8],2)-128, greenColorValue, "Green color does not match in testPixelColor")
		self.assertEqual(int(colorValue[16:24],2)-128, blueColorValue, "Blue color does not match in testPixelColor")


if __name__ == "__main__":
	unittest.main()
