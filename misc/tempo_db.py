"""
http://tempo-db.com/api/write-series/#write-series-by-key
"""

from datetime import datetime, timedelta
import random
from tempodb import Client, DataPoint

client = Client('a93feb1d6a7e49919331b09eab299967', '67fd4ee803df456b845cdeb5e675d465')

# for id in range(1,33):
#     station='station_'+str(id)
#     series = client.create_series(station)

date = datetime(2012, 1, 1)

for day in range(1, 10):
    # print out the current day we are sending data for
    print date

    for id in range(1,33):
        data = []
        # 1440 minutes in one day
        for min in range (1, 1441):
            data.append(DataPoint(date, random.random() * 50.0))
            date = date + timedelta(minutes=1)

        station='station_'+str(id)
        client.write_key(station, data)
