# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:21:39 2017

@author: Carnage
"""

import pyautogui
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

 

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False
driver = webdriver.Firefox(capabilities=capabilities)

driver.get("https://www.roblox.com/games/?SortFilter=1&TimeFilter=0&GenreFilter=1")

#moving from nth child to nth child gets you to the next list index using the selector
#GamesListContainer1 > div.games-list > ul > li:nth-child(3) > div > a
#GamesListContainer1 > div.games-list > ul > li:nth-child(4) > div > a
#GamesListContainer1 > div.games-list > ul > li:nth-child(4) > div > a > div.game-card-thumb-container > img
#GamesListContainer1 > div.games-list > ul > li:nth-child(4)



#href for click to work right under the expand li 
#GamesListContainer1 > div.games-list > ul > li:nth-child(4) > div

""" try saving nth child to variable and then using the class to click into the link"""
#driver.find_element_by_xpath('//*[@id="tab-about"]/a/span').click()

driver.find_element_by_xpath('//*[@id="GamesListContainer1"]/div[2]/ul/li[3]/div/a').click()
#or even you could do a iterator loop for click at //*[@id="GamesListContainer1"]/div[2]/ul/li['''i''']/div/a 
'''//*[@id="GamesListContainer1"]/div[2]/ul/li[2]/div/a'''

#saveas = ActionChains(driver).key_down(Keys.CONTROL)\
#         .key_down('s').key_up(Keys.CONTROL).key_up('s')
#saveas.perform()

#put the below into a def to write to file
'''
pyautogui.hotkey('ctrl', 's')
time.sleep(1)   
pyautogui.typewrite("test")
time.sleep(1)
pyautogui.hotkey('enter')

print("done")
'''
