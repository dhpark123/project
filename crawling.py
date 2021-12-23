import selenium
from selenium import webdriver as wd
from selenium.webdriver import ActionChains as AC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip as PC

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait







# url 지정
url = 'https://www.5gcamp.com/'

# user id, pw 지정
uid = 'eogks0300'
pwd = 'eogks001'

# Chrome 옵션 추가
options = wd.ChromeOptions()

# driver 등록
# driver = wd.Chrome(executable_path='C:/Users/list-pc28/Desktop/박대한/chromedriver_win32/chromedriver.exe')
driver = wd.Chrome(executable_path= 'D:/LiST/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)

log_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a')))
log_btn.click()
# <iframe id="fancybox-frame1629792020202" name="fancybox-frame1629792020202" class="fancybox-iframe" allowfullscreen="" allow="autoplay; fullscreen" src="./?mod=login&amp;iframe=Y" scrolling="no"></iframe>
# WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'fancybox-frame1629792020202')))
# WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'fancybox-frame1629792020202')))

frame = driver.find_element_by_name('fancybox-frame1629792020202')
driver.switch_to_frame(frame)

send_id = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.C, '//*[@id="id_input"]')))
send_id.click()
send_id.send_keys(uid)

send_pw = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass_input"]')))
send_pw.click()
send_pw.send_keys(pwd)


# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a'))).click()
# frame = WebDriverWait(driver, 30).until(EC.element_)
# driver.switch_to.frame(frame)
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_input"]'))).send_keys('eogks0300')
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass_input"]'))).send_keys('eogks001')


# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src='https://www.5gcamp.com//?mod=login&iframe=Y']")))
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_input"]'))).send_keys(uid)
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pass_input"]'))).send_keys(pwd)

# <iframe id="fancybox-frame1628563668816" name="fancybox-frame1628563668816" class="fancybox-iframe" allowfullscreen="" allow="autoplay; fullscreen" src="./?mod=login&amp;iframe=Y" scrolling="no"></iframe>



# driver.switch_to_frame('fancybox-frame1628563668816')


# fancybox = driver.find_element_by_id('fancybox-frame1628563668816')
# driver.switch_to.frame('fancybox')
# driver.implicitly_wait(5)



# elmt_id = driver.find_element_by_xpath('//*[@id="id_input"]')
# elmt_id.click()
# elmt_id.send_keys(uid)


# elmt_pw = driver.find_element_by_xpath('//*[@id="pass_input"]')
# elmt_pw.click()
# elmt_pw.send_keys(pwd)



# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a'))).click()
#
# driver.implicitly_wait(10)
# elmt_id = driver.find_element_by_css_selector('#pages_login > div.agreebox > form > div > div:nth-child(1) > label')
# elmt_id.clear()
# driver.implicitly_wait(10)
# elmt_id.send_keys('eogks0300')
# driver.implicitly_wait(10)
# elmt_pw = driver.find_element_by_css_selector('#pages_login > div.agreebox > form > div > div:nth-child(2) > label')
# elmt_pw.clear()
# driver.implicitly_wait(10)
# elmt_id.send_keys('eogks001')



# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a'))).click()
# driver.find_element_by_name('id').send_keys(uid)
# driver.find_element_by_name('pw').send_keys(pwd)

# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a'))).click()
# sendId = driver.find_element_by_xpath('//*[@id="pages_login"]/div[1]/form/div/div[1]/label')
# sendId.click()
# sendId.send_keys(uid)
#
# sendPw = driver.find_element_by_xpath('//*[@id="pages_login"]/div[1]/form/div/div[2]/label')
# sendPw.click()
# sendPw.send_keys(pwd)



# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a'))).click()
# driver.find_element_by_id('//*[@id="id_input"]').click()
# PC.copy(uid)
# AC(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
#
# driver.find_element_by_id('//*[@id="pass_input"]').click()
# PC.copy(pwd)
# AC(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()





# script_jquery_injection ='''
#     javascript:(function() {
#         function l(u, i) {
#             var d = document;
#             if (!d.getElementById(i)) {
#                 var s = d.createElement('script');
#                 s.src = u;
#                 s.id = i;
#                 d.body.appendChild(s);
#                 }
#             }
#             l('//code.jquery.com/jquery-3.2.1.min.js', 'jquery')
#         })();
# '''
# driver.execute_script(script_jquery_injection)








# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-full"]/div[1]/ul/li[4]/a'))).click()
# iframe = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fancybox-container-3"]/div[2]/div[4]/div/div')))
# driver.switch_to_frame(iframe)
# id_path = '//*[@id="id_input"]'
# pass_path = '//*[@id="pass_input"]'
# driver.find_element_by_xpath(id_path).send_keys(uid)
# driver.find_element_by_xpath(pass_path).send_keys(pwd)


# driver.execute_script(f'$("#id_input").val("eogks0300");')
# driver.execute_script(f'$("#pass_input").val("eogks001");')


# driver.execute_script(f'$("#id_input").val("' + uid + '");')
# driver.execute_script(f'$("#pass_input").val("' + pwd + '");')

# driver.execute_script("document.getElementById('SSLLoginform')[0].value='eogks0300'")
# driver.execute_script("document.getElementById('SSLLoginform')[1].value='eogks001'")

# driver.find_element_by_id('id_input').clear()
# driver.implicitly_wait(5)
# driver.find_element_by_id('id_input').send_keys(uid)
#
# driver.find_element_by_id('pass_input').clear()
# driver.implicitly_wait(5)
# driver.find_element_by_id('pass_input').sned_keys(pwd)


# send_id = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'id_input')))
# send_id.clear()
# send_id.send_keys(uid)
# send_pw = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'pass_input]')))
# send_pw.clear()
# send_pw.send_keys(pwd)
# WebDriverWait(driver, 5).until(EC.element_to_be_selected((By.XPATH, '//*[@id="id_input"]'))).send_keys(uid)
# WebDriverWait(driver, 5).until(EC.element_to_be_selected((By.XPATH, '//*[@id="pass_input"]'))).send_keys(pwd)