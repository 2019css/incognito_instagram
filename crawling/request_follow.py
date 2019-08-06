from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
from sys import platform as p_os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OS_ENV = "windows" if p_os == "win32" else "osx" if p_os == "darwin" else "linux"

if len(sys.argv) != 2:
    sys.exit('input two parameter')

chromedriver_min_version = 2.36
specific_chromedriver = "chromedriver_{}".format(OS_ENV)
chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

if not os.path.exists(chromedriver_location):
    chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
id = 'seoultechcss'
pw = 'csslab716'

user_id = sys.argv[1]
driver = webdriver.Chrome(chromedriver_location)
driver.implicitly_wait(3)
driver.get(url)
driver.implicitly_wait(1)
# login
driver.find_element_by_name('username').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
driver.implicitly_wait(3)
#remove popup
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()

#go to user
driver.get('https://www.instagram.com/{}/'.format(user_id))
driver.implicitly_wait(1)
#click follow
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()