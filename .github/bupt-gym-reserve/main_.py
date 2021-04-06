import os
import crontab
import time

cnt = 100
n = 0

while n < cnt:
    n = n + 1;
    time.sleep(2)
    os.system("python3 main.py -u ${{ secrets.BUPT_USERNAME }} -p ${{ secrets.BUPT_PASSWORD }};");
    
