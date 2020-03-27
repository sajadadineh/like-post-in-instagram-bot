from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import constants
import pass

option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome(Chrome_options=option, executable_path='./chromedriver')
driver.get(constants.base_url)

def login():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.log_in).click()
    sleep(2)
    username_element = driver.find_element_by_xpath(constants.username)
    username_element.clear()
    username_element.send_keys(pass.username)
    password_element = driver.find_element_by_xpath(constants.password)
    password_element.clear()
    password_element.send_keys(pass.password)
    password_element.send_keys(Keys.ENTER)
    sleep(2)

def notNowButton():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.not_now_button).click()
    sleep(2)

def findHashtag():
    driver.get(constants.hashtag_url.format("HASHTAG"))
    sleep(2)
    driver.implicitly_wait(20)

def clickPostAndLike():
    driver.find_element_by_xpath(constants.click_post).click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.like).click()
    scroll = driver
    


def closeDriver():
    driver.close()

login()
notNowButton()
findHashtag()
clickPostAndLike()