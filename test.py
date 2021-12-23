import os
import time
import warnings
warnings.filterwarnings('ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

id, pw = map(str, input("청소년진흥원 홈페이지에 접속했습니다.\nID와 PW를 입력해주세요! (구분: ',') : ").split(','))

url = 'https://www.youth.go.kr'

options = webdriver.ChromeOptions()
options.add_argument('--start-fullscreen')


driver = webdriver.Chrome('venv/chromedriver', options = options)
driver.get(url)
time.sleep(1)

driver.get('https://www.youth.go.kr/youth/eYouth/main/loginForm.yt;jsessionid=K5zLzek2Qd4OKNjajhvooUGq9JPKcCHfb1WqnAT1ENG834uJp93bGN11Q5Jqa8b0.youth-was02_servlet_kywaYouth')
time.sleep(1)

driver.find_element_by_name('mberId').send_keys(id)
pw_btn = driver.find_element_by_name('password')
pw_btn.send_keys(pw)
pw_btn.send_keys(Keys.RETURN)
time.sleep(1)
driver.get(url)
time.sleep(1)

# 업무지원서비스 클릭
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[3]/a').click()
time.sleep(1)
# 신고/인증/일반활동 클릭
driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/a').click()
time.sleep(1)
# 수련활동 인증 클릭
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()
time.sleep(1)
# 인증프로그램 운영관리 클릭
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[7]/a').click()
time.sleep(1)
# 운영프로그램 현황 클릭
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[7]/ul/li[1]/a').click()

driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[1]/select').click()
driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[1]/select/option[5]').click()

chk_list = list()
# chk_gen_min = int(str(min(chk_list)).lstrip('0'))
# chk_md_min = int(str(min(chk_list)).lstrip('MD'))
sel_list = [1,2]
state = 1
path = '/Users/dyani/Desktop/DyANi/청소년진흥원 폴더 생성/'

try:
    # 처음과 끝번호 입력받기
    first, end = map(int, input('다운받을 폴더의 처음과 끝 번호를 입력해주세요! : ').split(','))
    # 숫자 입력이 아니거나 처음번호가 끝번호가 클 경우 에러
    if type(first) != int or type(end) != int:
        raise TypeError
    elif first > end:
        raise NotImplementedError
except TypeError:
    print('숫자가 아닌 다른 걸 입력하지 않으셨나 확인해보시겠어요?')
except NotImplementedError:
    print('처음번호를 끝번호보다 작게 입력해주시겠어요?')
else:
    # 일반번호 or MD 선택!
    try:
        sel_num = int(input('|1. 일반번호 2. MD| : '))
        if sel_num not in sel_list:
            raise ValueError
    except ValueError:
        print('1 또는 2만 입력하세요!')
    else:
        # 1 또는 2 선택 시 정상 실행의 경우 실행되는 프로그램
        # 일반은 0으로 채우고, MD는 4자리 까지는 0 나머지는 MD
        for chk_num in range(first, end+1):
            if sel_num == 1:
                chk_num = str(chk_num).rjust(5, '0')
            else:
                chk_num = str(chk_num).rjust(4, '0')
                chk_num = str(chk_num).rjust(5, 'D')
                chk_num = str(chk_num).rjust(6, 'M')
            chk_list.append(chk_num)
        while len(chk_list) != 0:
            if sel_num == 1:
                if end < 5001:
                    # 맨 끝번호로 이동
                    driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[6]/a/span/span[2]').click()
                    # 맨 끝번호에서의 첫 번호의 정보 저장
                    start_tg = driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-27"]/td[2]/div').text
                    start_str = str(start_tg[-5:0]).lstrip('0')
                    start_str = float(start_str)
                    start_num = int(start_str)
                    # 처음 번호의 인증번호가 '1'일 때에는 27번의 태그까지밖에 없어 27번 반복하고
                    # chk_list에 있으면 폴더 생성, 없으면 다음 페이지 sch_num == 0,
                    # sch_num == 27고, 170이상의 차이면 페이지 대폭 넘김
                    if start_num == 1:
                        for sch_num in range(0, 28, -1):
                            first_tg = driver.find_element_by_xpath(f'//*[@id="datagrid-row-r2-2-{sch_num}"]/td[2]/div').text
                            first_id = first_tg[-5:0]
                            first_str = str(first_id)
                            if first_id in chk_list:
                                first_fcityNm = driver.find_element_by_xpath(f'//*[@id="datagrid-row-r2-2-{sch_num}"]/td[4]/div').text
                                os.makedirs(f'{path}{first_id}.{first_fcityNm}')
                            else:
                                if sch_num == 27 and (int(first) - start_num) > 170:
                                    driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[4]/a[6]/span/span').click()
                                    time.sleep(2)
                                elif sch_num == 0 :
                                    driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[4]/a[6]/span/span').click()
                                    time.sleep(2)
                                else:
                                    pass
                                continue
                    else:
                        # 첫페이지가 아닐 경우에,
                        #
                        for sch_num in range(0,50, -1):
                            crtfcId_tg = driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[2]/div').text
                            crtfcId_str = crtfcId_tg[-5:0]
                            crtfcId_num = int(str(crtfcId_str).lstrip('0'))
                            #579 429 -> 130  179  -> 230
                            if (first - crtfcId_num) > 230 :
                                driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[4]/a[1]/span/span').click()
                                time.sleep(2)
                            elif (first - crtfcId_num) > 130:
                                driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[4]/a[3]/span/span').click()
                                time.sleep(2)
                            else:
                                if crtfcId_str in chk_list :
                                    fcityNm = driver.find_element_by_xpath(f'//*[@id="datagrid-row-r2-2-{sch_num}"]/td[4]/div').text
                                    os.makedirs(f'{path}{crtfcId_str}.{fcityNm}')
                                else:
                                    if sch_num == 0:
                                        driver.find_element_by_xpath('//*[@id="listForm"]/div/div[3]/div/div/div[2]/table/tbody/tr/td[3]/a/span/span[2]').click()
                                        time.sleep(2)
                                    else:
                                        continue
                # end > 5001
                else:
                    pass
            # MD
            else:
                pass


driver.quit()

