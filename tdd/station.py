from station_details import StationDetails
import sys        

for i in range(31,33):
    data=[]
    s=StationDetails(id=i)
    s.get_details()
    data.append(s)
    
    for station in data:
        print repr(station.id).rjust(2),
        print repr(station.available).rjust(5),
        print repr(station.empty).rjust(5),
        print str(station.time).rjust(30)

    
