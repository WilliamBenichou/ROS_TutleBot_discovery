#!/usr/bin/env python3

import rospy

from std_msgs.msg import Float32
from kobuki_msgs.msg import Sound




def callback(data):
    if data < 0:
        #invalid distance
    else:
        #valid distance

    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/min_dist", Float32, callback)

    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
    listener()