from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import constants

option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome(options=option, executable_path='./chromedriver')
driver.get(constants.base_url)

def login():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.log_in).click()
    sleep(2)
    username_element = driver.find_element_by_xpath(constants.username)
    username_element.clear()
    username_element.send_keys("YOUR USERNAME")
    password_element = driver.find_element_by_xpath(constants.password)
    password_element.clear()
    password_element.send_keys("YOUR PASSWORD")
    password_element.send_keys(Keys.ENTER)
    sleep(2)

def notNowButton():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.not_now_button).click()
    sleep(2)

def findHashtag():
    driver.get(constants.hashtag_url.format("HASHTAG"))
    driver.implicitly_wait(20)


login()
notNowButton()
findHashtag()