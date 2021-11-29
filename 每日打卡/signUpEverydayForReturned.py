import requests
import json
import time

def sign_in():

    session = {'JSESSIONID':"自己抓", 
               'SESSION': '自己抓',
               'Hm_lvt_fe3b7a223fc08c795f0f4b6350703e6f': str(int(time.time())),
               'Hm_lpvt_fe3b7a223fc08c795f0f4b6350703e6f': str(int(time.time()))
               }
    url = 'https://jzsz.uestc.edu.cn/wxvacation/monitorRegisterForReturned'
    data = {
    "healthCondition": "正常",
    "todayMorningTemperature": "36°C~36.5°C",
    "yesterdayEveningTemperature": "36°C~36.5°C",
    "yesterdayMiddayTemperature": "36°C~36.5°C",
    "location": "四川省成都市郫都区"
    }
    head = {'Content-Type':'application/json', 'charset':'utf-8', 'x-tag': 'flyio'}
    r = requests.post(url, cookies=session, headers=head, data=json.dumps(data))
    print(r.json())

if __name__ == '__main__':
    sign_in()
