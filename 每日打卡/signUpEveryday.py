import requests
import json

def sign_in():
    session = {'JSESSIONID':'自己抓'}
    url = 'https://xgaffairs.uestc.edu.cn/wxvacation/monitorRegister'
    data = {
    "currentAddress":"xx市xx区xx小区",
    "remark":"",
    "healthInfo":"正常",
    "isContactWuhan":0,
    "isFever":0,
    "isInSchool":0,
    "isLeaveChengdu":1,
    "isSymptom":0,
    "temperature":"36.5°C~36.9°C",
    "province":"xx省",
    "city":"xx市",
    "county":"xx区"
    }
    head = {'Content-Type':'application/json', 'charset':'utf-8'}
    r = requests.post(url, cookies=session, headers=head, data=json.dumps(data))
    print(r.json())

if __name__ == '__main__':
    sign_in()