# import library
from statistics import mode
from urllib import request
import pandas as pd
import json, datetime, time

# 326 -> 337  #338#
req_url = 'http://18.135.15.186:5000/v1/sensors?upper_latitude=100&upper_longitude=50&lower_latitude=51&lower_longitude=-40'  #&page=1&perPage=5'
# while True:
for _ in range(24):
    req_response = request.urlopen(req_url).read()
    print(req_url)
    req_response = json.loads(req_response)

    req_response = req_response['results']
    req_response = pd.DataFrame(req_response)
    # req_response['dt'] = datetime.timestamp
    req_response.insert(loc=0, column='dt', value=int(datetime.datetime.now().timestamp()))
    req_response.insert(loc=1, column='date', value=datetime.datetime.now().date())
    req_response.insert(loc=2, column='time', value=datetime.datetime.now().time())
    dayoftheweek = datetime.datetime.strptime(str(datetime.datetime.now().date()), '%Y-%m-%d').strftime('%A')
    req_response.insert(loc=3, column='dayoftheweek', value=dayoftheweek)

    req_response.to_csv('data/aq/aqData.csv', index=None)
    # print(req_response)
    time.sleep(60 * 60) # 1hour

