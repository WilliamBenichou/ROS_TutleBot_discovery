#!/usr/bin/env python3
import rospy
import math
import time
from std_msgs.msg import Float32
from kobuki_msgs.msg import Sound

class BipBipRadar:
    frequency_low = 0.33
    frequency_high = 10
    frequency_touch = 20

    delay_low = 1/frequency_low
    delay_high = 1/frequency_high
    delay_touch = 1/frequency_touch

    enabled = False
    currDelay = delay_low

    def __init__(self):
        self.pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)

    def run(self):
        while(not rospy.is_shutdown()):
            if(self.enabled):
                time.sleep(self.currDelay)
                sound = Sound()
                sound.value = sound.BUTTON
                self.pub.publish(sound)
            else:
                time.sleep(0.1) #wait


    def callback(self, data):
        value = data.data
        print(value)
        if value > 0.0:
            #invalid distance
            if(value > 2.0):
                self.enabled = False
            else:
                self.enabled = True
                
                lerpValue = (value - 0.5)/1.5
                if(lerpValue < 0.0):
                    lerpValue = 0
                elif(lerpValue > 1.0):
                    lerpValue = 1

                self.currDelay = self.delay_low + (self.delay_high - self.delay_low) * (1-lerpValue)


        else:
            #valid distance
            self.enabled = True  
            self.currDelay = self.delay_touch

        
def listener(callback):
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/min_dist", Float32, callback)

if __name__ == '__main__':
    radar = BipBipRadar()
    listener(radar.callback)
    radar.run()
    rospy.spin()