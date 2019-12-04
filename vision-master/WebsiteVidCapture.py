from selenium import webdriver
from PIL import Image
from main import execute
#from moviepy.editor import *
import time
import cv2
import os
import sys

def run(website_name):
	driver = webdriver.Chrome(executable_path='~/Desktop/chromedriver')
	#https://nyctmc.org/google_popup.php?cid=975
	driver.get(website_name)
	strTime = str(time.time())
	image_folder = '~/Desktop/vision-master/' + strTime
	os.mkdir(image_folder)
	os.chdir(image_folder)

	#take multiple screenshots
	#figure out how many duplicates you need
	for x in range(20):
		time.sleep(1)
		driver.save_screenshot(str(time.time()) + ".png")

	driver.close()


	video_name = 'video.avi'

	images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
	images.sort()

	left = 848
	top = 127
	right = 1552
	down = 541
	width = right - left
	height = down - top
	video = cv2.VideoWriter(video_name, 0, 1, (width, height))
	
	for image in images:
		im = Image.open(image)
		crop = im.crop((left, top, right, down))
		crop.save(image)
		video.write(cv2.imread(os.path.join(image_folder, image)))

	cv2.destroyAllWindows()
	video.release()
	for image in images:
                os.remove(image)

	return strTime
arg1 = sys.argv[1]

while(1>0):
	strTime = run(arg1)
	os.chdir('~/Desktop/vision-master/'+strTime)
	tup = execute('~/Desktop/vision-master/'+strTime, "video.avi", "result", 2)
	print("up: " + str(tup[0]) + " down: " + str(tup[-1]))