import time
import requests
from tqdm import tqdm
import sys

def install():
	print("Welcome to codepad plugin, do you want to install the plugin?\n This will affect the notepad and change some assets, not only, if your notepad version is more than 1.0b, it will make your version downgrade and be 1.0b. You can even lose some plugins(if you have some). If you'll update the notepad it will remove this plugin.(y/n)?")
	choice=input("> ")
	if choice == "y" or choice == "Y" or choice == "yes" or choice == "Yes":
	   url = 'https://csnotes-plugins.netlify.app/plugins/content-codepad.txt'
	   ext = '.nc'
	   print('Getting Url..')
	   response = requests.get(url)
	   content = response.text
	   f=open('../../main.py', 'w')
	   for char in tqdm(content):
	   	time.sleep(0.00035)
	   f.write(content)
	   f.close()
	   nf = open('../../data/pl.txt', 'w')
	   nf.write('python')
	   nf.close()
	   print('Process completed.')
	   time.sleep(3)
	   sys.exit(0)
	else:
		print("Process denied.")
		input("[press enter to quit]")
		quit()
	
install()
