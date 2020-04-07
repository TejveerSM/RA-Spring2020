from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from beautifulsoupextractor import extractor
import time

# enter the initial URL
url = "https://www.youtube.com/watch?v=oUJbuFMyBDk"

# open the web browser
driver = webdriver.Chrome('C:/Academics/RA_Spring_2020/chromedriver.exe')

for i in range(100):

	# open the given URL
	driver.get(url)

	# wait for 10 seconds before thowing a timeout exception unless the element is found
	# title of the video
	wait = WebDriverWait(driver, 10)
	title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
	#print('Title:', title)

	# length of the video
	length = driver.find_element_by_class_name("ytp-time-duration").text
	#print('Length:', length)

	# send the url and the length to the extractor method
	# extractor method in beautifulsoup.py file will extract the other details
	extractor(url, length)

	# to see the progress on the output screen
	print(i+1)

	# find the next button and click it
	elem = driver.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]')
	elem.click()

	# wait for 5 seconds (to give some time for the new video to load)
	time.sleep(5)

	# get the URL of the new video
	url = driver.current_url

print ('----------Extraction complete----------')

#close the browser
driver.quit()