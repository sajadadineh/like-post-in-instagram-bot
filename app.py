from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import datetime
import constants

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option, executable_path='./chromedriver')
driver.maximize_window()
driver.get(constants.base_url)

username = raw_input("please Enter your username : ")
password = raw_input("please Enter your password : ")
hashtag = raw_input("please Enter the hashtag you want : " )

def closeDriver():
    driver.close()

def login():
    driver.implicitly_wait(20)
    try:
        driver.find_element_by_xpath(constants.username).send_keys(username)
        driver.find_element_by_xpath(constants.password).send_keys(password,Keys.ENTER)
    except:
        print(">>>Signup failed\n>>>It may be a problem with your username or password")

def notNowButton():
    try:
        driver.implicitly_wait(20)
        driver.find_element_by_xpath(constants.not_now_button)
        print(">>>login successfuly")
    except:
        print(">>>login successfuly")

def findHashtag():
    try:
        driver.implicitly_wait(20)
        driver.get(constants.hashtag_url.format(hashtag))
        print(">>>find you hashtag")
    except:
        print(">>>hashtag not found")

def clickPostAndLike():
    driver.implicitly_wait(20)
    print(">>>start like post")
    driver.find_element_by_xpath(constants.click_post).click()
    num_like = 0
    while True:
        sleep(2)
        driver.find_element_by_xpath(constants.like).click()
        num_like += 1
        driver.find_element_by_xpath(constants.next_button).click()
        if(num_like == 300): # the limitations of Instagram are met "350 Likes per hour"
            print(">>>sleep up to 1 hour")
            sleep(3600)
            print(">>>start like post again")
            num_like = 0


login()
notNowButton()
findHashtag()
try:
    clickPostAndLike()
except:
    print("like finished")
    closeDriver()