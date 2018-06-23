import requests
import json
import time
from random import randint

url = "http://100.98.44.21:8002/scheduler/"

while True:
    dltput = str(randint(500,1400))
    rsrp = str(randint(60, 80))
    sinr = str(randint(0, 20))
    print dltput, rsrp, sinr
    requests.post(url, data = json.dumps({'cmd':"dltput", "data":{"dltput":dltput}}, ensure_ascii=False)) 
    requests.post(url, data = json.dumps({'cmd':"rsrp", "data":{"rsrp":rsrp}}, ensure_ascii=False)) 
    requests.post(url, data = json.dumps({'cmd':"sinr", "data":{"sinr":sinr}}, ensure_ascii=False))
    time.sleep(2) 

