import webbrowser
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen

# method to get the video details
def extractor(url, length):

	# opens the network object at the given url and reads 
	webpage = urlopen(url).read()

	# passing the webpage object to the BeautifulSoup constructor to get HTML output
	soup = BeautifulSoup(webpage, 'html.parser')

	# dictionary to store the video details
	video_details = {}

	# getting the required details
	# soup.findAll returns a list of all the elements with the given tag and class name
 	for span in soup.findAll('span',attrs={'class': 'watch-title'}):
	    video_details['TITLE'] = span.text.strip()

	video_details['LENGTH'] = length

	for div in soup.findAll('div',attrs={'class': 'watch-view-count'}):
	    video_details['NUMBER_OF_VIEWS'] = div.text.strip()

	for button in soup.findAll('button',attrs={'title': 'I like this'}):
	    video_details['LIKES'] = button.text.strip()

	for button in soup.findAll('button',attrs={'title': 'I dislike this'}):
	    video_details['DISLIKES'] = button.text.strip()

	for span in soup.findAll('span',attrs={'class': 'yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count'}):
	    video_details['NUMBER_OF_SUBSCRIPTIONS'] = span.text.strip()

	for script in soup.findAll('script',attrs={'type': 'application/ld+json'}):
	        channelDesctiption = json.loads(script.text.strip())
	        video_details['CHANNEL_NAME'] = channelDesctiption['itemListElement'][0]['item']['name']
	
	# save the details to a file	        
	with open('video_details.json', 'a', encoding='utf8') as outfile:
	    json.dump(video_details, outfile, ensure_ascii=False, indent=4)