from bs4 import BeautifulSoup

def get_info(type,number):
    stations = open("stations.xml","r")
    soup = BeautifulSoup(stations.read(),'xml')
    info=''
    if( (type == 'name') or (type == 'address') or (type == 'lat') or (type == 'lng')):
        for stat in soup.carto.markers.findAll("marker"):
            if(stat['number']==str(number)):
                info=stat[type]
    stations.close()
    return info

if __name__ == '__main__':
    for i in range(1,33):
        print 'Station_'+str(i).zfill(2)+': ',
        print get_info(type='name',number=i)+", ",
        print get_info(type='address',number=i)+", ",
        print get_info(type='lat',number=i)+", ",
        print get_info(type='lng',number=i)
