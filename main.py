import os
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
warnings.filterwarnings("ignore")

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

url = 'https://www.youth.go.kr'

id, pw = map(str, input("청소년활동진흥원 홈페이지에 접속하려합니다!\nID와 PW를 입력해주세요(구분:',') : ").split(','))

options = webdriver.ChromeOptions()
options.add_argument('--start-fullscreen')
# options.add_argument('headless')
# options.add_argument('no-sandbox')
# 개발환경이 리눅스의 경우에 사용하면 좋은 옵션!
options.add_argument('disable-gpu')
# options.add_argument('lang=ko_KR')
# options.add_argument('user-argent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome('./chromedriver', options=options)
driver.get(url)
time.sleep(2)
log_btn = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[3]/ul/li[1]/a')
# log_btn.click()
driver.get('https://www.youth.go.kr/youth/eYouth/main/loginForm.yt;jsessionid=Kra1vRPzq6iYjBlLFszO8xX3uVMriV5YqRwWlxXP0vF1Q27ap5MJcLbI1zUIKU11.youth-was02_servlet_kywaYouth®')

# 로그인을 위한 입력받은 아이디와 패스워드 보내기
driver.find_element_by_name('mberId').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
time.sleep(2)
# 로그인 버튼
log_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/fieldset/div/button')
log_btn.send_keys(Keys.RETURN)
time.sleep(2)
driver.get(url)
time.sleep(2)

# 청소년활동진흥원 홈페이지 '업무지원서비스' 클릭!
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[3]/a').click()
time.sleep(1)
# '신고/인증/일반활동' 클릭!
driver.find_element_by_xpath('//*[@id="header"]/div[2]/ul/li[1]/a').click()
time.sleep(1)
# '수련활동 인증' 클릭!
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/a').click()
time.sleep(1)
# '인증프로그램 운영관리' 클릭!
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[7]/a').click()
time.sleep(1)
# '운영프로그램 현황' 클릭!
driver.find_element_by_xpath('//*[@id="nav"]/li[2]/ul/li[7]/ul/li[1]/a').click()
time.sleep(1)
# 'crtfcId' - 인증번호, 'fcityNm' - 운영기관

sel_list = [1, 2]
state = 1
while state == 1:
    first, end = map(int, input("청소년활동진흥원 원천데이터 수집을 위한 폴더 생성 준비를 마쳤습니다.\n처음과 끝으로 생성할 인증번호를 입력해주세요(구분','): ").split(','))
    try:
        sel_Num = int(input('1.MD일 경우, 2.일반일 경우 : '))
        if sel_Num not in sel_list:
            raise ValueError
            continue
        else:
            for crtfcIdNum in range(first, end + 1):
                # '인증번호' 입력!
                crtfcId = driver.find_element_by_xpath(
                    '//*[@id="listForm"]/div/div[1]/div[1]/table/tbody/tr[2]/td[1]/span/input[1]')
                crtfcId.clear()
                print('인증번호를 위치를 가져왔습니다')
                time.sleep(3)
                if sel_Num == 1:
                    crtfcIdNum = str(crtfcIdNum).rjust(4, "0")
                    crtfcIdNum = str(crtfcIdNum).rjust(5, "D")
                    crtfcIdNum = str(crtfcIdNum).rjust(6, "M")
                    crtfcId.send_keys(crtfcIdNum)
                    time.sleep(1)
                elif sel_Num == 2:
                    # 문자열 채우기 (zfill(0으로 채울 횟수), rjust(채울 횟수),(채울 문자열)) - 문자열 앞에 특정 문자로 채워넣기
                    crtfcIdNum = str(crtfcIdNum).rjust(5, "0")
                    crtfcId.send_keys(crtfcIdNum)
                    time.sleep(1)
                print('인증번호를 보냈습니다')
                # '검색' 클릭!
                sch_btn = driver.find_element_by_xpath('//*[@id="listForm"]/div/div[1]/div[2]/a')
                print('검색버튼의 위치를 가져왔습니다')
                sch_btn.send_keys(Keys.RETURN)
                time.sleep(1)
                print('검색을 완료했습니다')
                # '운영기관명' 가져오기!
                fcityNm_tg = driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[4]/div')
                fcityNm = fcityNm_tg.text
                os.makedirs(f'{path}/{crtfcIdNum}.{fcityNm}')
                print('가져온 인증번호와 운영기관명으로 폴더 생성을 완료했습니다')
                pass
            try:
                say_Yes = str(input("추가로 다운받으시려면 '네'를 입력해주세요! : "))
                if say_Yes != '네':
                    raise ValueError
            except ValueError:
                print("'네'가 아닌 다른 걸 입력하셔서 프로그램을 종료합니다!")
                state = 0
    except ValueError:
        print('1 또는 2만 입력할 수 있습니다!')
driver.quit()