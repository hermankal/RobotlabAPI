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
    cam_change_ref_object(ip, id)
    time.sleep(3)
    return cam_get_result(ip)
    
def cam_get_xy(ip):
    coords = cam_get_result(ip).decode('utf-8')
    x = coords.split(",")
    y = x[1].split(")")
    y = float(y[0])
    x = x[0].split("(")
    x = float(x[1])
    return {"x": x, "y": y}
    
def cam_convert_xy(x, y, offsetx, offsety):
    if (x == 0.00 and y == 0.00):
        return "No object found"
    x = (x + offsetx) /1000
    y = (x + offsety) /1000
    return {"x": x, "y": y}
    
def cam_get_xy_and_convert(ip, offsetx, offsety):
    coords = cam_get_xy(ip)
    return cam_convert_xy(coords["x"], coords["y"], offsetx, offsety)
    
# http://192.168.1.110/LiveImage.jpg
def cam_get_jpg(ip):
    page = urllib.request.urlopen("http://" + ip + "/LiveImage.jpg")
    return page