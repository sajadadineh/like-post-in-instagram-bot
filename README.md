# like-post-in-instagram

### Description

This Python program is a robot that likes the images of a hashtag

### Advantages

- In this robot, the limitations of Instagram are met "350 Likes per hour"
- selenium
- python
- use mobileEmulation
- headless

## How to use it?

1.Install python, pip, virtualenv

2.Clone the project `git clone https://github.com/sajadadineh/like-post-in-instagram-bot.git`

3.Create a virtualenv `virtualenv -p python3 venv`

4.Connect to virtualenv `source venv/bin/activate`

5.install packages using `pip install -r requirements.txt`

6.Download a Web Driver from [Selenium](https://www.selenium.dev/downloads/) and set in helper class

`driver = webdriver.Chrome(executable_path='YOUR WEB DRIVER',chrome_options= option)`

7.Run by `python app.py`
