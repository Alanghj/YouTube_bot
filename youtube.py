from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from youtube_cl import YouTube
import pandas as pd
import random
import time

MUSIC_NAME = 'Sad music'

def youtube_bot_path():

    driver = webdriver.Chrome()
    driver.get("http://www.youtube.com/")

    # Search the element

    path = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
    click = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(MUSIC_NAME)

    youtube = YouTube(path, click)

    youtube.link_path(path)
    youtube.click_path(click)

    # # Click the search bar
    time.sleep(2)
    click = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
    youtube.click_path(click)

    # # Find the video
    dt = pd.read_json("youtube_list.json")
    pathies = random.choice(dt['links'])
    time.sleep(2)
    click = driver.find_element_by_xpath(pathies).click()
    youtube.click_path(click)
    

    # # Skip the video
    time.sleep(10)
    click = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button').click()
    youtube.click_path(click)
    

    time.sleep(3600)
    driver.quit()


if __name__ == '__main__':
    youtube_bot_path()