import requests
import json

def sign_in():
    session = {'JSESSIONID':'自己抓'}
    url = 'https://xgaffairs.uestc.edu.cn/wxvacation/monitorRegisterForReturned'
    data = {
	"healthCondition": "正常",
	"todayMorningTemperature": "36°C~36.5°C",
	"yesterdayEveningTemperature": "36°C~36.5°C",
	"yesterdayMiddayTemperature": "36°C~36.5°C"
    }
    head = {'Content-Type':'application/json', 'charset':'utf-8', 'x-tag': 'flyio'}
    r = requests.post(url, cookies=session, headers=head, data=json.dumps(data))
    print(r.json())

if __name__ == '__main__':
    sign_in()