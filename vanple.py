from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import re


url = "https://www.5gcamp.com/?c=5g"
# url = 'https://www.5gcamp.com/?c=5g/?mod=login&iframe=Y'

# url = str(input('URL 입력:'))
options = wd.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
# driver = wd.Chrome(executable_path='D:/LiST/chromedriver_win32/chromedriver.exe')
# , options=options

driver = wd.PhantomJS('D:/LiST/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.implicitly_wait(3)


# uid = str(input('ID 입력:'))
# pwd = str(input('PW 입력:'))
# uid = 'eogks0300'
# pwd = 'eogks001'

driver.get(url)
driver.maximize_window()
WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/ul/li[4]/a'))).click()
# driver.find_element_by_xpath("""//*[@id="header-full"]/div[1]/ul/li[4]/a""").click()
send_id = driver.find_element_by_css_selector("#pages_login > div.agreebox > form > div > div:nth-child(1) > label")
send_id.send_keys('eogks0300')
send_pw = driver.find_element_by_css_selector("#pages_login > div.agreebox > form > div > div:nth-child(2) > label")
send_pw.send_keys('eogks001')
driver.find_element_by_xpath("""//*[@id="pages_login"]/div[1]/form/div/div[1]/label""").click()
# WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pages_login"]/div[1]/form/div/div[1]/label'))).click()

# element.send_keys(uid)
# element.click()
# element.send_keys(pwd)
print('로그인 성공!')
driver.close()

# /Users/dyani/PycharmProjects/pythonProject/collaboration/samsung