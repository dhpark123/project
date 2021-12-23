from datetime import datetime

datetime_str = str(input("'YYYY-MM-DD'의 형식으로 날짜를 입력해주세요 : "))
datetime_date = datetime.strptime(datetime_str, '%Y-%m-%d')
datetime_time_str = str(input("'HH:MM 24H 표기법'의 형식으로 입력해주세요 : "))
datetime_time_time = datetime.strptime(datetime_time_str, '%H:%M')
print(datetime_date)
print(type(datetime_date))
print(str(datetime_date)[0:10])
print(str(datetime_time_str))
print(str(datetime_time_str)[11:19])