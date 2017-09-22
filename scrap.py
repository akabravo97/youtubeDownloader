#from pyvirtualdisplay import Display
import requests
import os
import webbrowser
import tkinter
from selenium import webdriver
import time
#display=Display(visible=0)
#display.start()
i=0
key=input('Enter search term:')
br=webdriver.Firefox(executable_path='D:\\geckodriver.exe')
home=br.get('https://www.youtube.com/results?search_query='+key)
time.sleep(20)
videoTitle=br.find_elements_by_id('video-title')
for var in videoTitle:
    j=i+1
    i=i+1
    print(str(j)+'. '+var.text)
ch=input('Enter video number to download:')
chno=int(ch)
chno=chno-1
videoTitle[chno].click()
time.sleep(5)
YT_url=br.current_url
br.get('http://en.savefrom.net/1-how-to-download-youtube-video/')
time.sleep(7)
linkBox=br.find_element_by_id('sf_url')
linkBox.send_keys(YT_url)
arrowButton=br.find_element_by_id('sf_submit')
arrowButton.click()
time.sleep(5)
downloadButton=br.find_element_by_class_name('def-btn-box')
downloadButton.click()
#display.stop()