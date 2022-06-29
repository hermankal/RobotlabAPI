import time
import requests

def sensor_proximity(port):
    p = 0
    r = requests.post("http://10.1.1.9", json={"code":"request","cid":1,"adr":"/getdatamulti","data":{"datatosend":["/iolinkmaster/port[" + str(port) + "]/iolinkdevice/pdin"]}})
    res = r.json()
    res1 = res['data']
    data = str(res1)
    if data[53] == "2":
        d = data[68]+data[69]
        p = float(int(d,16))
    else:
        p = 0
    return p