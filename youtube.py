from elements import pathies, click, click_2, click_3, click_4
from youtube_cl import YouTube
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

MUSIC_NAME = 'Sad music'

def youtube_bot_path():

    driver = webdriver.Chrome()
    driver.get("http://www.youtube.com/")

    # Search the element

    # path = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
    # click = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(MUSIC_NAME)

    youtube = YouTube(pathies, click)

    youtube.link_path(pathies)
    youtube.click_path(click)

    # # Click the search bar
    time.sleep(2)
    # click = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
    youtube.click_path(click_2)

    # # Find the video
    time.sleep(2)
    # click = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/ytd-thumbnail/a/yt-img-shadow/img').click()
    youtube.click_path(click_3)
    

    # # Skip the video
    time.sleep(8)
    # click = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button').click()
    youtube.click_path(click_4)
    

    time.sleep(3600)
    driver.quit()


if __name__ == '__main__':
    youtube_bot_path()