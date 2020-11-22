#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Empty
from kobuki_msgs.msg import Led

# IMPORTANT: Ce code n'a pas été testé car réalisé or des heures de TP (sans turtlebot à disposition)

class BlinkRadar:
    blinkDuration = 0.03 #blink faster than maximum frequency (Support 33Hz max)
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/distance_warning_blink", Empty, self.callback)
        self.pub_led = rospy.Publisher('/mobile_base/commands/led1', Led, queue_size=10)

    def callback(self, data):
        #should trigger led
        ledmsg = Led()
        ledmsg.value = ledmsg.GREEN
        self.pub_led.publish(ledmsg)

        time.sleep(self.blinkDuration)

        ledmsg.value = ledmsg.BLACK
        self.pub_led.publish(ledmsg)

if __name__ == '__main__':
    radar = BlinkRadar()
    rospy.spin()