import time
import requests
from retrying import retry
from confluent_kafka import Consumer

c = Consumer({'bootstrap.servers': 'kafka-1:9092',
              'group.id': 'myapp',
              'api.version.request': True,
              'log.connection.close': False,
              'socket.keepalive.enable': True,
              'session.timeout.ms': 6000,
              'default.topic.config': {'auto.offset.reset': 'smallest'}})

@retry(wait_fixed=10000)
def scrape_station_status():
    r = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
    if r.status_code != 200:
         raise IOError("station status fetch failed!")
    return r.json()	

while True:
    data = scrape_station_status()
    for i in data['data']['stations']:
        c.subscribe([i])
        citibike.station.update = c.consume(timeout=10000)
