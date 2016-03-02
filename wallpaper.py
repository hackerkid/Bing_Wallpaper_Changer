import urllib2
import json
import datetime
import os.path, time
from os.path import expanduser
import gconf
import os
import commands
market = 'en-US'
resolution = '1920x1080'
Dir = expanduser("~" + '/usr/share/backgrounds')
WallpaperName = 'wallpaper.jpg'

def setw():
	os.system('gsettings set org.gnome.desktop.background picture-uri file://' + Dir + WallpaperName)
	return
	

l=1
while (l==1):
	try:
		urllib2.urlopen("http://google.com")
	except urllib2.URLError, e:
		time.sleep(10)
	else:
		l=0

		response = urllib2.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=" + market)
		obj = json.load(response)
		#print(obj)
		url = (obj['images'][0]['urlbase'])
		#print(url)
		url = 'http://www.bing.com' + url + '_' + resolution + '.jpg'
		#print(url)
		if not os.path.exists(Dir):
			os.makedirs(Dir)
		path = Dir + WallpaperName
		print("Downloading")
		f = open(path,'w')
		bingpic = urllib2.urlopen(url)
		f.write(bingpic.read())
		setw()
