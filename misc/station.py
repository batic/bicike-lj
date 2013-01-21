from station_details import StationDetails
import sys        

print 'id' + 5*' ' + 'avail' +5*' ' + 'free' + 5*' ' + 'tot' + 5*' '+ 'time'
for i in range(1,33):
    data=[]
    s=StationDetails(id=i)
    s.get_details()
    data.append(s)

    for station in data:
        print repr(station.id).rjust(2),
        print repr(station.available).rjust(5),
        print repr(station.empty).rjust(5),
        print repr(station.total).rjust(5),
        print str(station.time).rjust(30),
        print station.name

    
