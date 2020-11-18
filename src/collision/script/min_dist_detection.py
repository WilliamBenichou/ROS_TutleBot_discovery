#!/usr/bin/env python3
import rospy
import math

from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32


def callback(data):
    min_range = -1 
    #safety init preveting crash if no valid value detected
    #crash when trying to publish uninitialized float in /min_dist
    for range in data.ranges:
        if not math.isnan(range):
            min_range = range
            break
    for range in data.ranges:
        if not math.isnan(range):
            if range < min_range:
                min_range = range
    rospy.loginfo(rospy.get_caller_id() + "I heard " +  str(min_range))
    pub.publish(min_range)
    
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/scan", LaserScan, callback)
    
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/min_dist', Float32, queue_size=10)
    listener()