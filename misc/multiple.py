from datetime import datetime
import time
from tempodb import Client, DataPoint
from apscheduler.scheduler import Scheduler
from station_details import StationDetails
from collections import defaultdict

data = defaultdict(list)

def get_station():
    for i in range(1,6):
        s=StationDetails(id=i)
        s.get_details()

        #print repr(s.id).rjust(2),
        #print repr(s.available).rjust(5),
        #print repr(s.empty).rjust(5),
        #print str(s.time).rjust(30)
    
        data[s.id].append(DataPoint(s.time, s.available))

def print_data(tdata):
    for station in tdata:
        for datapoint in tdata[station]:
            print station,
            print ':',
            print datapoint

def push_data():
    print_data(temp_data)
    temp_data=data.copy
    print_data(temp_data)


if __name__ == '__main__':
    for r in range(1,4):
        get_station()
        time.sleep(2)
    
    print "Data:"
    print_data(data)
    print "Tempdata:"
    temp_data=data.copy()
    data.clear()
       
    print_data(temp_data)
    print "Data:"
    print_data(data)
    

