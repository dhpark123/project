#################################################################################################################
# < 라이브러리 > 1. 파일 생성을 위한 라이브러리, 2. 주소 및 태그 정보를 가져올 때의 걸리는 시간을 고려하여 텀을 주기 위한 라이브러리         #
# 3. send_keys를 이용한 행동 메시지를 감추기 위한 라이브러리                                                                #
##################################################################################################################
import os #1
import shutil
import time #2
import warnings #3
warnings.filterwarnings('ignore')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# WebDriverWait을 사용하기 위한 라이브러리
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
url = 'https://www.youth.go.kr'
try:
    id, pw = map(str, input("청소년활동진흥원 홈페이지에 접속했습니다.\n로그인을 위한 ID와 PW를 입력해주세요! (구분: ',') : ").split(','))
except Exception:
    print('아이디 또는 비밀번호가 일치하지 않나봅니다! 다시 입력해보실래요?')

options = webdriver.ChromeOptions()
options.add_argument('--start-fullscreen')

driver = webdriver.Chrome('venv/chromedriver', options=options)
driver.get(url)
time.sleep(2)

login_page = 'https://www.youth.go.kr/youth/eYouth/main/loginForm.yt'
driver.get(login_page)
driver.find_element_by_name('mberId').send_keys(id)
pw_tg = driver.find_element_by_name('password')
pw_tg.send_keys(pw)
pw_tg.send_keys(Keys.RETURN)

driver.get('https://www.youth.go.kr')
# '업무지원서비스'
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[3]/a').click()
time.sleep(1)
# '신고/인증/일반활동'
driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/a').click()
time.sleep(1)
# '수련활동 인증'
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()
time.sleep(1)
# '인증프로그램 운영관리'
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[7]/a').click()
time.sleep(1)
# '운영프로그램 현황'
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[7]/ul/li[1]/a').click()
time.sleep(1)

# Page_Button
page_btn = driver.find_element_by_class_name('pagination-page-list')
page_btn.click()
time.sleep(1)
page_five = driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[1]/select/option[5]')
page_five.click()
time.sleep(1)

state = 1
crtfcId_list = list()
chk_list = list()
sel_list = [1,2]
path = '/Users/dyani/Desktop/DyANi/청소년진흥원 폴더 생성'


while state == 1:
    try:
        first, end = map(int, input("생성하고 싶은 폴더의 처음과 끝 번호를 입력해주세요 (구분: ',') : ").split(','))
        if type(first) != int or type(end) != int:
            raise TypeError
        elif first > end :
            raise NotImplementedError
        else:
            try:
                sel_Num = int(input('|1. 일반번호  2. MD|  : '))
                if sel_Num not in sel_list:
                    raise ValueError
            except ValueError:
                print('1 또는 2만 입력하세요!')
            else:
                # 다운받을 인증번호 생성
                for chk_Num in range(first, end + 1):
                    # 일반 혹은 MD 선택!
                    if sel_Num == 1:
                        chk_Num = str(chk_Num).rjust(5, '0')
                    else:
                        chk_Num = str(chk_Num).rjust(4, '0')
                        chk_Num = str(chk_Num).rjust(5, 'D')
                        chk_Num = str(chk_Num).rjust(6, 'M')
                    chk_list.append(chk_Num)
                print(chk_list)
                while len(chk_list) != 0:
                    for sch_Num in range(0, 50):
                        crtfcId_tg = driver.find_element_by_xpath(
                            f'//*[@id="datagrid-row-r2-2-{sch_Num}"]/td[2]/div')
                        crtfcId_text = crtfcId_tg.text
                        if sel_Num == 1:
                            crtfcId_str = crtfcId_text[-5:]
                            print(crtfcId_str)
                            if crtfcId_str in chk_list:
                                fcity_tg = driver.find_element_by_xpath(
                                    f'//*[@id="datagrid-row-r2-2-{sch_Num}"]/td[4]/div')
                                fcityNm = fcity_tg.text
                                os.makedirs(f'{path}/{crtfcId_str}.{fcityNm}')
                                chk_list.remove(crtfcId_str)
                                print('폴더를 생성했습니다!!!')
                            elif sch_Num == 49:
                                nxt_btn = driver.find_element_by_xpath(
                                    '//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[5]/a/span/span[2]')
                                nxt_btn.click()
                                time.sleep(2)
                            else:
                                continue
                        else:
                            crtfcId_str = crtfcId_text[-6:]
                            if crtfcId_str in chk_list:
                                fcity_tg = driver.find_element_by_xpath(
                                    f'//*[@id="datagrid-row-r2-2-{sch_Num}"]/td[4]/div')
                                fcityNm = fcity_tg.text
                                os.makedirs(f'{path}/{crtfcId_str}.{fcityNm}')
                                chk_list.remove(crtfcId_str)
                                print('폴더를 생성했습니다...')
                            elif sch_Num == 49:
                                nxt_btn = driver.find_element_by_xpath(
                                    '//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[5]/a/span/span[2]')
                                nxt_btn.click()
                                time.sleep(2)
                            else:
                                continue


                try:
                    doubt_Yes = str(input("'혹시 잘못 다운 받으셨나요? 폴더를 비워드릴까요? ('네')"))
                    if type(doubt_Yes) != str:
                        raise TypeError
                    elif doubt_Yes == '네':
                        shutil.rmtree(path)
                        continue
                    else:
                        print('실수가 아닌걸로 알고? 그냥 넘어갈게요?')
                        try:
                            say_Yes = str(input("다시 다운로드 받으실래요? ('네') : "))
                            if type(say_Yes) != str:
                                raise TypeError
                        except TypeError:
                            print('문자열이 아닌 다른 걸 입력하셨어요 다시 입력해주세요!')
                        if say_Yes == '네':
                            continue
                        else:
                            print("'네'가 아닌 다른 걸 입력하셔서 프로그램을 종료합니다!!")
                            break
                        continue
                except TypeError:
                    print('문자열 이외의 입력은 받질 않아요~')

    except TypeError:
        print('정수형 숫자 이외의 입력은 받지 않습니다!')
    except NotImplementedError:
        print('처음과 끝을 반대로 입력하셨나본데요?')

driver.quit()