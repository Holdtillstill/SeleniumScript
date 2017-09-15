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


#==============================================================================
# Working Code here
#==============================================================================

driver = webdriver.Chrome()

homePageString = "https://www.roblox.com/games/?SortFilter=1&TimeFilter=0&GenreFilter=1"

home = driver.get(homePageString)

def main():
   
    count = 1
    x = True
    
    while x == True:
        #in the string %(keys)s will be replaced with count
        Xpath = '//*[@id="GamesListContainer1"]/div[2]/ul/li[%(key)s]/div/a'
        Xpath %= {'key':count}
        #clicks the first page and then iterates through the rest and does the same thing
        clickXpath(Xpath)
        #about page
        clickXpath('//*[@id="tab-about"]/a')
        aboutUrl = getUrl()
        savePage(aboutUrl)
        time.sleep(1)
        #store page
        clickXpath('//*[@id="tab-store"]/a')
        storeUrl = getUrl()
        savePage(storeUrl)
        time.sleep(1)
        #leaderboards
        clickXpath('//*[@id="tab-leaderboards"]/a')
        leaderboardUrl = getUrl()
        savePage(leaderboardUrl)   
        time.sleep(1)
        count += 1
        pyautogui.hotkey('alt','left')
        pyautogui.hotkey('alt','left')
        pyautogui.hotkey('alt','left')
        pyautogui.hotkey('alt','left')
   
#==============================================================================
# things to do     
#==============================================================================

'''
find out how to save it in one single directory
find out how to save it as one single html file instead of html and resource files
'''

#==============================================================================
# things done
#==============================================================================
#first xpath to be looped through    
'''//*[@id="GamesListContainer1"]/div[2]/ul/li[1]/div/a'''  
#vs + li[i] to be iterated through
'''//*[@id="GamesListContainer1"]/div[2]/ul/li[63]/div/a'''
#xpaths of the 3 pages to be saved in a roblox app 
#//*[@id="tab-about"]/a
#//*[@id="tab-store"]/a
#//*[@id="tab-leaderboards"]/a

#==============================================================================
# functions
#==============================================================================

'''to make this script less hardcoded change the unwanted str variable to remove 
unwanted generic url address text for better naming conventions  '''
def getUrl():
    unwantedString = 'https://www.roblox.com/games/'
    
    dirtyURL = str(driver.current_url)
    cleanURL = dirtyURL.replace(unwantedString,'').replace('!','').replace('/','_')
    
    return cleanURL

#write html to file definition
def savePage(URL):
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)   
    pyautogui.typewrite(URL)
    time.sleep(1)
    pyautogui.hotkey('enter')
    
#xpath click definition
def clickXpath(path):
    driver.find_element_by_xpath(path).click()

#==============================================================================
# test code starts here   
#==============================================================================

#moving from nth child to nth child gets you to the next list index using the selector
#GamesListContainer1 > div.games-list > ul > li:nth-child(3) > div > a
#GamesListContainer1 > div.games-list > ul > li:nth-child(4) > div > a
#GamesListContainer1 > div.games-list > ul > li:nth-child(4) > div > a > div.game-card-thumb-container > img
#GamesListContainer1 > div.games-list > ul > li:nth-child(4)



#href for click to work right under the expand li 
#GamesListContainer1 > div.games-list > ul > li:nth-child(4) > div


    
""" try saving nth child to variable and then using the class to click into the link"""
#driver.find_element_by_xpath('//*[@id="tab-about"]/a/span').click()

#driver.find_element_by_xpath('//*[@id="GamesListContainer1"]/div[2]/ul/li[3]/div/a').click()
#or even you could do a iterator loop for click at //*[@id="GamesListContainer1"]/div[2]/ul/li['''i''']/div/a 
'''//*[@id="GamesListContainer1"]/div[2]/ul/li[2]/div/a'''

#print(driver.current_url)
#print(getUrl())

#==============================================================================
# ends here
#==============================================================================

if __name__ == '__main__':
    main()
