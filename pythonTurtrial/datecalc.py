from datetime import datetime, timedelta

"""calc N days after"""
base_date = datetime(2025,2,27) + timedelta(days=3)
print(base_date.strftime('%y/%m/%d'))

"""calc remein seconds"""
Sleep_time_seconds = datetime(2025,4,4,8,30,0) - datetime(2025,4,3,22,0,0)
print('睡眠時間は' + str(Sleep_time_seconds.seconds/3600) + '時間です')

"""calc remein days"""
date = datetime(2025,4,3) - datetime.now()
print('あと' + str(date.days + 1) + '日です')

"""display current date"""
time = datetime.now()
print(time.strftime('%Y年%m月%d日 %H時%M分%S秒'))