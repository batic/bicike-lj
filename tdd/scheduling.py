"""
Basic example showing how the scheduler integrates with the application it's
running alongside with.
"""
from datetime import datetime
import time
from tempodb import Client, DataPoint
from apscheduler.scheduler import Scheduler
from station_details import StationDetails
from collections import defaultdict

#bicike(lj) tempodb database:
client = Client('40349331c03d4d4e9c544f812af291a9', 'f6e1594584a74f28ae00a872cd179462')
data=defaultdict(list)

def push_data():
    print(' --- now in push_data() --- \n')
    #make copy to push and clear the original (thread safe??? probably not)
    push_data=data.copy() 
    data.clear()

    if False:
        for station in push_data:
            for datapoint in push_data[station]:
                print station,
                print ':',
                print datapoint

    #add push to the tempodb server
    for station in push_data:
        key="Station_"+str(station).zfill(2)
        client.write_key(key,push_data[station])

    push_data.clear()
                
def get_station():
    #print(' --- now in get_station() --- ')
    for i in range(1,33):
        s=StationDetails(id=i)
        s.get_details()
        data[s.id].append(DataPoint(s.time, s.available))

if __name__ == '__main__':
    scheduler = Scheduler()
    #scheduler.add_interval_job(tick, seconds=2)
    scheduler.add_interval_job(get_station, seconds=60)
    scheduler.add_interval_job(push_data, seconds=1200)
    print('Press Ctrl+C to exit')
    scheduler.start()

    # This is here to simulate application activity (which keeps the main
    # thread alive).
    while True:
        print('\rThe programm is still running ...')
        time.sleep(60)
