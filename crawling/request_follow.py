from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys

if len(sys.argv) != 2:
    sys.exit('input two parameter')

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
id = 'seoultechcss'
pw = 'csslab716'
user_id = sys.argv[1]
driver = webdriver.Chrome('C:\\Users\\happy\\Desktop\\git\\incognito_instagram\\crawling\\chromedriver.exe')
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