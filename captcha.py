from PIL import Image
from PIL import ImageEnhance
from pytesser import *
import urllib 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

x = webdriver.Chrome()
	x.get('')                  ##1

	get_captcha(x)
	
def get_captcha(x):
	element = x.find_element_by_id('')   ##2
	location = element.location
	size = element.size
	x.save_screenshot('screenshot.png') ##3
	#x.quit()

	im = Image.open('screenshot.png') 

	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']


	im = im.crop((left, top, right, bottom)) 
	im.save('screenshot.png') 

	image = Image.open("screenshot.png")
	
	nx, ny = image.size
	im2 = image.resize((int(nx), int(ny)), Image.BICUBIC)
	#im2.save("temp2.png")
	
	


	im2.save('temp.tif')                 ##4 
	image_file = 'temp.tif'
	im = Image.open(image_file)
	text = image_to_string(im)
	text = image_file_to_string(image_file)
	text = image_file_to_string(image_file, graceful_errors=True)
	text = text.strip()
	text = unicode(text,"utf-8").lower()
	print "#################\n"
	print ">>>>"+text+"<<<<<"
