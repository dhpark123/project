from datetime import datetime
import time

now = datetime.now()
# 기능 1
# 캘린더 형식 운동 기록 그 날 시간 기록 날짜
# 기능 2
# 기능 3
# 기능 4

# 컬럼
# 기상시간, 취침시간, 컨디션 상태, 피곤함 정도,

chest_list = []
arm_list = []
back_list = []
leg_list = []
hip_list = []

# 상태에 대한 변수
state = 1
# 기존 기능에 대한 선택번호 초기화
sel_list = [1,2,3,4]
# 컬럼명 넣기 위한 리스트 초기화
col_list = list()
# 각 컬럼에 맞게 넣을 리스트 초기화
app_list = list()
# 컨디션과 피로함 정도의 값 초기화
yN_list = ['Y', 'y', 'N', 'n']
kin_list = ['가슴', '등', '어깨', '엉덩이', '팔', '다리']
con_list = ['상', '중상', '중', '중하', '하']
ftg_list = ['상', '중', '하']

while state == 1:
    try:
        sel_num = int(input('어떤 기능을 이용하시겠어요?\n1.기록\n'))
        if type(sel_num) != int:
            raise TypeError
        elif sel_num not in sel_list:
            raise ValueError


    except TypeError:
        print("숫자가 아닌 다른 걸 입력하셨어요!")
    except ValueError:
        print('지정된 번호만 입력하실 수 있어요!')
    else:
        if sel_num == 1:
            try:
                date_Yn = str(input('날짜를 수기 등록하실래요? (Y/n)'))
                if date_Yn not in yN_list :
                    raise ValueError
            except ValueError:
                print('지정된 형식에 맞는 입력을 해주세요!')
            else:
                if date_Yn == 'n' or date_Yn == 'N':
                    today_date = now.strftime('%Y-%m-%d')
                    col_list.append(today_date)
                else:
                    try:
                        today_str1 = str(input('1995-06-29 | 위와 같은 표기 방법에 맞게 작성해주세요\n : '))
                        today_date = datetime.strptime(today_str1, "%Y-%m-%d")
                        today_str2 = str(input('24:00 | 위와 같은 표기 방법에 맞게 작성해주세요\n : '))
                        today_time = datetime.strptime(today_str2, "%H:%m")
                        # 1995가
                        if int(today_str1) != int or today_str2 != int:
                            raise TypeError
                    except TypeError :
                        print('숫자를 입력해주셔야 해요! 문자열을 입력하신 것 같아요!')
                    else:

            print('오늘의 날짜 등록을 완료했습니다!')
            time.sleep(.5)
            today_wtime = now.strftime('%H:%M')
            col_list.append(today_wtime)
            print('현재 시각을 기점으로 기상시간을 등록하였습니다!')
            time.sleep(.5)
            try:
                workout_kind = str(input('운동 부위 : '))
                if workout_kind not in kin_list:
                    raise ValueError
                elif type(workout_kind) != str:
                    raise TypeError
            except ValueError:
                print('지정된 형식을 벗어난 입력이에요!')
            except TypeError:
                print('문자열 이외의 입력을 했어요!')
            else:
                try:
                    workout_set = int(input('세트 수 : '))
                    if type(workout_set) != int:
                        raise TypeError
                except TypeError:
                    print('세트 수를 위한 숫자를 입력해주세요!')
                else:
                    try:
                        workout_cnt = int(input('횟수 : '))
                        if type(workout_cnt):
                            raise TypeError
                    except TypeError:
                        print('횟수를 위한 숫자를 입력해주세요!')
                    else:
                        try:
                            print('끝으로 취침시간을 등록하려고 합니다.\n수기 등록하실래요? :')
                        except:

                        else:

        elif sel_num == 2:
            print('아직 기능이 구현되지 않았어요! 2번!')
        elif sel_num == 3:
            print('아직 기능이 구현되지 않았어요! 3번!')
        else:
            print('아직 기능이 구현되지 않았어요! 4번!')
