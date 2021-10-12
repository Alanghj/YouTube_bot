from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=aES24Io9XLI')

try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button'))
    element_present.click()
    WebDriverWait(driver, 5).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
