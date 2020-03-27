from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import constants

username = raw_input("please Enter your username : ")
password = raw_input("please Enter your password : ")

option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver')
driver.get(constants.base_url)

def login():
    driver.implicitly_wait(20)
    driver.find_element_by_xpath(constants.username).send_keys(username)
    driver.find_element_by_xpath(constants.password).send_keys(password,Keys.ENTER)
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
# notNowButton()
# findHashtag()
# clickPostAndLike()