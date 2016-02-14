from time import sleep
from myo import init, Hub, DeviceListener
import requests, urllib2

adjval = 0

class Listener(DeviceListener):

    def on_pair(self, myo, timestamp, firmware_version):
        print("Hello, Myo!")

    def on_unpair(self, myo, timestamp):
        print("Goodbye, Myo!")

    def on_orientation_data(self, myo, timestamp, quat):
        print("Orientation:", quat.x, quat.y)
        adjval = (quat.x + 1) * 7.5
        print adjval
        #r = requests.post("http://pi.michaelbailey.co/control", data = {"dc":adjval})
        response = urllib2.urlopen('http://pi.michaelbailey.co/control?dc='+str(adjval))
        html = response.read()


init()
hub = Hub()
hub.run(1000, Listener())
try:
    while True:
        sleep(0.5)
except KeyboardInterrupt:
    print('\nQuit')
finally:
    hub.shutdown()  # !! crucial
