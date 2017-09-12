# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:21:39 2017

@author: Carnage
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyautogui
import time 

driver = webdriver.Firefox()

driver.get("https://www.roblox.com/games/606849621/Jailbreak-Thank-You#!/leaderboards")

driver.find_element_by_xpath('//*[@id="tab-about"]/a/span').click()

#saveas = ActionChains(driver).key_down(Keys.CONTROL)\
#         .key_down('s').key_up(Keys.CONTROL).key_up('s')
#saveas.perform()

pyautogui.hotkey('ctrl', 's')
time.sleep(1)   
pyautogui.typewrite("test")
time.sleep(1)
pyautogui.hotkey('enter')

print("done")
