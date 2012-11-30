from datetime import datetime
from bs4 import BeautifulSoup
import urllib2

class StationDetails(object):
    """ A simple class for Station details data"""

    def __init__(self,id):
        if id and ( id>0 ) and (id<=32):
            self.id = id
        else:
            self.id = 1
        self.available = None
        self.total = None
        self.empty = None
        self.time = None

    def __eq__(self, other):
        return self.id == other.id and self.available == other.available and self.total == other.total and self.empty == other.empty and self.time == other.time

    def get_details(self):
        station_url='http://www.bicikelj.si/service/stationdetails/ljubljana/'
        station_url += str(self.id)
        
        station_data = urllib2.urlopen(station_url,timeout=60)
        soup = BeautifulSoup(station_data, "xml")
        
        self.available=int(soup.station.available.text)
        self.empty=int(soup.station.free.text)
        self.total=int(soup.station.total.text)
        self.time=datetime.now()

    def Print(self):
        print("Station id      = " + str(self.id))
        print("Available bikes = " + str(self.available))
        print("Empty locks     = " + str(self.empty))
        print("Total spaces    = " + str(self.total))
        print("Data retrieved  = " + str(self.time))


