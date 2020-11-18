#!/usr/bin/env python3
import rospy

# Import custom message data.
from kobuki_msgs.msg import BumperEvent, Sound



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard " +  str(data))
    if (data.state == 1):
        s = Sound()
        s.value = s.ON
        pub.publish(s)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, callback)
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
    listener()
