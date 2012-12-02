"""
Basic example showing how the scheduler integrates with the application it's
running alongside with.
"""
from datetime import datetime
import time
from tempodb import Client, DataPoint
from apscheduler.scheduler import Scheduler
from station_details import StationDetails

#bicike(lj) tempodb database:
client = Client('40349331c03d4d4e9c544f812af291a9', 'f6e1594584a74f28ae00a872cd179462')
data=[] #list of data points

def push_data():
    #make copy to push and clear the original (thread safe??? probably not)
    push_data=data 
    data=[]

    for stations in push_data:
        print repr(stations.id).rjust(2),
        print repr(stations.available).rjust(5),
        print repr(stations.empty).rjust(5),
        print str(stations.time).rjust(30)

def get_station():
    for i in range(1,6):
        s=StationDetails(id=i)
        s.get_details()

        # print repr(s.id).rjust(2),
        # print repr(s.available).rjust(5),
        # print repr(s.empty).rjust(5),
        # print str(s.time).rjust(30)
    
        data[s.id].append(DataPoint(s.time, s.available))

if __name__ == '__main__':
    scheduler = Scheduler()
    #scheduler.add_interval_job(tick, seconds=2)
    scheduler.add_interval_job(get_station, seconds=30)
    scheduler.add_interval_job(push_data, seconds=120)
    print('Press Ctrl+C to exit')
    scheduler.start()

    # This is here to simulate application activity (which keeps the main
    # thread alive).
    while True:
        print('This is the main thread.')
        time.sleep(10)
