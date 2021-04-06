
import crontab

cnt = 100
n = 0

while n < cnt:
    n = n + 1;
    echo sleep 1;
    echo python3 main.py -u ${{ secrets.BUPT_USERNAME }} -p ${{ secrets.BUPT_PASSWORD }};
    
