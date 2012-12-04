from tempodb import Client, DataPoint

client = Client('40349331c03d4d4e9c544f812af291a9', 'f6e1594584a74f28ae00a872cd179462')

for id in range(1,33):
    station='station_'+str(id).zfill(2)
    series = client.create_series(station)
