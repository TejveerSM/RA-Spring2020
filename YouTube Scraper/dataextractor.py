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

#initial URL
webpage = urlopen("https://www.youtube.com/watch?v=TcMBFSGVi1c").read()

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
#print(soup, file=open("soup.txt", "w"))
print(html, file=open("html2.txt", "w"))

for i in range(3):

	video_details = {}

	# used for appending
	next_link = 'https://www.youtube.com/'

	for span in soup.findAll('span',attrs={'class': 'watch-title'}):
	    video_details['TITLE'] = span.text.strip()

	for span in soup.findAll('span',attrs={'class': 'accessible-description'}):
	    video_details['DURATION'] = span.text.strip()
	    break

	for span in soup.findAll('span',attrs={'class': 'video-time'}):
	    video_details['LENGTH'] = span.text.strip()
	    break

	for script in soup.findAll('script',attrs={'type': 'application/ld+json'}):
	        channelDesctiption = json.loads(script.text.strip())
	        video_details['CHANNEL_NAME'] = channelDesctiption['itemListElement'][0]['item']['name']

	for div in soup.findAll('div',attrs={'class': 'watch-view-count'}):
	    video_details['NUMBER_OF_VIEWS'] = div.text.strip()

	for button in soup.findAll('button',attrs={'title': 'I like this'}):
	    video_details['LIKES'] = button.text.strip()

	for button in soup.findAll('button',attrs={'title': 'I dislike this'}):
	    video_details['DISLIKES'] = button.text.strip()

	for span in soup.findAll('span',attrs={'class': 'yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count'}):
	    video_details['NUMBER_OF_SUBSCRIPTIONS'] = span.text.strip()

	# gets a list of similar videos, .get('href') gives the URL
	for a in soup.findAll('a',attrs={'class': 'content-link spf-link yt-uix-sessionlink spf-link'}):
	    next_link = next_link + a.get('href')
	    print(i+1)
	    break

	with open('data_2.json', 'a', encoding='utf8') as outfile:
	    json.dump(video_details, outfile, ensure_ascii=False, indent=4)

	# to open the next video URL
	webpage = urlopen(next_link).read()
	soup = BeautifulSoup(webpage, 'html.parser')

print ('----------Extraction of data is complete. Check json file.----------')