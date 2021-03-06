#!/usr/bin/python

import re, csv, subprocess, urllib, select

from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output

import solver
from python_anticaptcha import AnticaptchaClient, ImageToTextTask

if __name__=="__main__":

	url='https://service.mail.com/registration.html'

	# profile = webdriver.FirefoxProfile()
	# profile.accept_untrusted_certs = True
 #    profile.default_preferences["webdriver_assume_untrusted_issuer"] = false
 #    profile.update_preferences()
	# driver = webdriver.Firefox(firefox_profile=profile, executable_path='/Users/doronshai/code/geckodriver')
	options = Options()
	# options.add_argument("--headless")
	driver = webdriver.Firefox(firefox_options=options, executable_path='/Users/doronshai/code/geckodriver')

	# driverJS = webdriver.PhantomJS('/Users/doronshai/code/capcha/phantomjs-2.1.1-macosx/bin/phantomjs', service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

	print('Get URL')
	driver.get(url)

	# Get the main windows ID
	mainWin = driver.current_window_handle  



	print('Fill Login details and change Captcha')
	# driver.find_element_by_css_selector("input[class='Text ColouredFocus']").send_keys("james");
	driver.find_element_by_xpath('//*[@id="idb"]').send_keys("james")
	driver.find_element_by_xpath('//*[@id="idd"]').send_keys("brown")
	driver.find_element_by_xpath('//*[@id="idf"]/option[text()="Male"]').click()	
	driver.find_element_by_xpath('//*[@id="id14"]/option[text()="Mar"]').click()
	driver.find_element_by_xpath('//*[@id="id11"]/option[text()="19"]').click()
	driver.find_element_by_xpath('//*[@id="id15"]/option[text()="1981"]').click()
	driver.find_element_by_xpath('//*[@id="id16"]/option[text()="Hungary"]').click()
	driver.find_element_by_xpath('//*[@id="id1e"]').send_keys("james.brown.1981")

	driver.find_element_by_xpath('//*[@label="Top Choices"]/option[text()="writeme.com"]').click()

	driver.find_element_by_xpath('//*[@id="id2c"]').send_keys("Aa123456")
	driver.find_element_by_xpath('//*[@id="id2f"]').send_keys("Aa123456")
	driver.find_element_by_xpath('//*[@id="id34"]').send_keys("oobarnashoo@gmail.com")
	driver.find_element_by_xpath('//*[@id="id37"]/option[text()="What city were you born in?"]').click()

	driver.find_element_by_xpath('//*[@id="id39"]').send_keys("Mambo Jambo")

	sleep(10)

	# driver.find_element_by_id("id51").send_keys("lulu")


	# driver.find_element_by_xpath('//*[@id="switchCaptcha"]').click()

	# print('Handle screenshot')
	# element = driver.find_element_by_id('adcopy-puzzle-image')
	# location = element.location
	# size = element.size
	# driver.save_screenshot('screenshot.png') # saves screenshot of entire page
	# im = Image.open('screenshot.png') # uses PIL library to open image in memory
	# im = im.convert("RGB")	
	# left = location['x']
	# top = location['y']
	# right = location['x'] + size['width']
	# bottom = location['y'] + size['height']
	# im = im.crop((left, top, right, bottom)) # defines crop points
	# im.save('screenshot.png') # saves new cropped image

	# api_key = 'ffe2af874e4ceac6029155d90cccca85'
	# captcha_fp = open('screenshot.png', 'rb')
	# client = AnticaptchaClient(api_key)
	# task = ImageToTextTask(captcha_fp)
	# job = client.createTask(task)
	# job.join()
	# print ('The solved captcha is - ' + job.get_captcha_text())
	# driver.find_element_by_id("adcopy_response").send_keys(job.get_captcha_text())
	# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/form/div[3]/div[1]/input').click()
	# print ('Logged in Successfully')
	# sleep(5)
	# print ('Close Advertisment')
	# driver.find_element_by_id("closebtn_ads").click()
	# sleep(10)
	# print ('Click for paid clicks')	
	# driver.find_element_by_xpath('//*[@id="t_menu"]/div/div[2]/div[1]/ul/li[1]/a').click()
	# sleep(5)	
	# print ('Click on Ad')	
	# driver.find_element_by_xpath('//*[@id="pagination_box_1"]/a[1]/div/div[2]/img').click()
	# sleep(6)	
	# # Switch to new Window for Ad Watching
	# window_after = driver.window_handles[1]
	# driver.switch_to_window(window_after)
 #    sleep(6)
	# # Close Ad Windows after viewed
 #   	driver.quit();
	# driver.switch_to_window(mainWin)

	driver.quit();
