from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from scripts.youtube_cl import YouTube
from tkinter import *
from tkinter import ttk
import random
import json
import time

MUSIC_NAME = 'Sad music'


def youtube_bot_path():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    start_music = ttk.Button(frm, text="Start Music").grid(column=0, row=1)
    print(start_music)

    if start_music:

        driver = webdriver.Chrome()
        driver.get("http://www.youtube.com/")

        # Search the element
        path = driver.find_element_by_xpath(
            '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
        click = driver.find_element_by_xpath(
            '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(MUSIC_NAME)
        youtube = YouTube(path, click)
        youtube.link_path(path)
        youtube.click_path(click)

        # # Click the search bar
        time.sleep(2)
        click = driver.find_element_by_xpath(
            '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
        youtube.click_path(click)

        # # Find the video
        with open('data_base/youtube_list.json') as f:
            data = json.load(f)
        pathies = random.choice(data['links'])
        time.sleep(2)
        click = driver.find_element_by_xpath(pathies).click()
        youtube.click_path(click)

        # # Skip the video
        time.sleep(10)
        click = driver.find_element_by_xpath(
            '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button').click()
        youtube.click_path(click)

    # End the bot actions
    # time.sleep(3600)
   
    end_music = ttk.Button(frm, text="End Music",
                           command=root.destroy).grid(column=0, row=2)

    root.mainloop()
    # ttk.Button(driver.quit())


if __name__ == '__main__':
    youtube_bot_path()
