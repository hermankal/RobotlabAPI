import requests

def sensor_proximity(port):
    proximity = 0
    r = requests.post("http://10.1.1.9", json={"code":"request","cid":1,"adr":"/getdatamulti","data":{"datatosend":["/iolinkmaster/port[" + str(port) + "]/iolinkdevice/pdin"]}})
    r = r.json()
    data = str(r['data'])
    if data[53] == "2":
        d = data[68] + data[69]
        proximity = float(int(d,16))
    else:
        proximity = 0
    return proximity