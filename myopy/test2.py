from time import sleep
from myo import init, Hub, DeviceListener
import requests, urllib2, sys

class Listener(DeviceListener):
    adjval = 0
    newx = 0
    temp = 0
    def on_pair(self, myo, timestamp, firmware_version):
        print("Hello Yas! Welcome to your therapy training! Let's begin!")
        sleep(1);
        print("Please raise your hand up.")

    def on_unpair(self, myo, timestamp):
        print("Goodbye, Myo!")

    def on_orientation_data(self, myo, timestamp, quat):
        print("Orientation:", quat.x, quat.y)

        #adjval = (quat.x + 1) * 7.5
        #print adjval
        #r = requests.post("http://pi.michaelbailey.co/control", data = {"dc":adjval})

        if (quat.x < Listener.temp):
            print("Raise your hand/n")
            sleep(1)
            Listener.temp = quat.x
        else:
            print("Lower your hand/n")
            sleep(1)
            Listener.temp = quat.x

        #     newx = 1
        #     Listener.temp = quat.x
        #     sleep(1)
        # else:
        #     newx = 15
        #     Listener.temp = quat.x
        #     sleep(1)
        # print newx
        # response = urllib2.urlopen('http://rpi.michaelbailey.co/control?dc='+str(newx))
        # html = response.read()




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
