import time
import datetime

post_time = datetime.datetime.now().second
time.sleep(10)
now_time = datetime.datetime.now().second

if post_time - now_time > 100:
    print("12133")

else:
    pass