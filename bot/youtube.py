from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import json


MUSIC_NAME = 'Sad music'


def youtube_bot_path():
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get("http://www.youtube.com/")

    # Search for element
    path = browser.find_element_by_xpath(
        '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    path.click()

    search_element = browser.find_element_by_xpath(
        '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search_element.send_keys(MUSIC_NAME)

    # Click the search bar
    search_bar = browser.find_element_by_xpath(
        '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search_bar.send_keys(Keys.ENTER)

    # File locations (../data_base/youtube_list.json) / data_base/youtube_list.json
    try:
        with open('data_base/youtube_list.json') as f:
            data = json.load(f)
    except ImportError:
        print('The element json was not found!')

    # Find the video
    path_videos = random.choice(data['links'])
    find_the_video = browser.find_element_by_xpath(path_videos)
    find_the_video.click()

    # Skip the video
    skip_video = browser.find_element_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button')
    skip_video.click()


if __name__ == '__main__':
    youtube_bot_path()
