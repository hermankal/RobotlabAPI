import time
import urllib.request

def cam_take_picture(ip):
    page = urllib.request.urlopen("http://" + ip + "/CmdChannel?TRIG")
    return "Request sent to http://" + ip + "/CmdChannel?TRIG"
   
def cam_get_result(ip):
    page = urllib.request.urlopen("http://" + ip + "/CmdChannel?gRES")
    return page.read()
   
def cam_change_ref_object(ip, id):
    page = urllib.request.urlopen("http://" + ip + "/CmdChannel?sINT_1_" + id)
    return "Request sent to http://" + ip + "/CmdChannel?sINT_1_" + id

def cam_change_ref_object_and_wait(ip, id):
    ret = cam_change_ref_object(ip, id)
    time.sleep(3)
    return ret
    
def cam_change_ref_object_and_get_result(ip, id):
    page = urllib.request.urlopen("http://" + ip + "/CmdChannel?sINT_1_" + id)
    time.sleep(3)
    return cam_get_result(ip)
    
def cam_get_xy(ip):
    page = urllib.request.urlopen("http://" + ip + "/CmdChannel?gRES")
    coords = page.read().decode('utf-8')
    x = coords.split(",")
    y = x[1].split(")")
    y = y[0]
    x = x[0].split("(")
    x = x[1]
    return {"x": x, "y": y}
    
def cam_convert_xy(x, y, offsetx, offsety):
    x = (float(x) + offsetx) /1000
    y = (float(y) + offsety) /1000
    return {"x": x, "y": y}
    
def cam_get_xy_and_convert(ip, offsetx, offsety):
    page = urllib.request.urlopen("http://" + ip + "/CmdChannel?gRES")
    coords = page.read().decode('utf-8')
    x = coords.split(",")
    y = x[1].split(")")
    y = y[0]
    x = x[0].split("(")
    x = x[1]
    x = (float(x) + offsetx) /1000
    y = (float(y) + offsety) /1000
    return {"x": x, "y": y}