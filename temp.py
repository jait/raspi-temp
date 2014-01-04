#!/usr/bin/python -tt
# vim: set et sw=4 sts=4:
import json
import time
import os

DEV = "28-000005852306"
#FILE = "/tmp/temp.json"
FILE = "/run/temp.json"

def read_temp(dev):
    """
    7c 01 4b 46 7f ff 04 10 09 : crc=09 YES
    7c 01 4b 46 7f ff 04 10 09 t=23750
    """
    tfile = open("/sys/bus/w1/devices/%s/w1_slave" % dev) 
    lines = tfile.readlines()
    tfile.close()
    if len(lines) < 2:
        raise Exception("Invalid file format")

    crc_ok = lines[0].strip().split(" ")[-1] == "YES"
    if not crc_ok:
        raise Exception("CRC failure")

    try:
        tempdata = lines[1].strip().split(" ")[9] 
        temp = float(tempdata[2:]) / 1000
        return temp
    except:
        raise


def write_file(temp):
    data = {'value': temp, 'timestamp': time.time()}
    newfilename = "%s.new" % FILE
    newfile = open(newfilename, "w")
    newfile.write(json.dumps(data))
    newfile.close()
    os.rename(newfilename, FILE)

if __name__ == '__main__':
    temp = read_temp(DEV)
    print temp
    write_file(temp)
