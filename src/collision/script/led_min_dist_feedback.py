#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Empty
from kobuki_msgs.msg import Led

class BlinkRadar:
    blinkDuration = 0.05
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/distance_warning_blink", Empty, self.callback)
        self.pub_led = rospy.Publisher('/mobile_base/commands/led1', Led, queue_size=10)

    def callback(self, data):
        #should trigger led
        ledmsg = Led()
        ledmsg.value = ledmsg

        
def listener(callback):
    

if __name__ == '__main__':
    radar = BlinkRadar()
    rospy.spin()