# 리눅스에만 가능
## 파일명 : cron01.py ###########################

# pip install apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def exec_interval(): # 일정시간 간격으로 수행
    print("hello world")

def exec_cron():
    str = time.strftime('%c',time.localtime(time.time()))
    print("cron",str)

sched = BlockingScheduler()
# 5초 간격으로 exec_interval() 함수 호출하기
sched.add_job(exec_interval, 'interval', seconds=60)

# 예약 방식 (매 시간 10초, 30초 일 경우 구동)
sched.add_job(exec_cron,'cron', minute="*", second="10,30")
sched.start()