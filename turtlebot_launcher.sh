echo "Checking if host is online: 192.168.1.204"
nc -z 192.168.1.204 22 > /dev/null

if [ $? -eq 0 ]
then
    echo "Host is online"
    echo "Launching ROS-core..."
    terminator -e 'ssh turtlebot@192.168.1.204 turtlebot ; roscore' -p hold
    terminator -e 'ssh turtlebot@192.168.1.204 turtlebot ; roslaunch turtlebot2i_bringup minimal.launch' -p hold --new-tab
    terminator -e 'ssh turtlebot@192.168.1.204 turtlebot ; roslaunch turtlebot2i_bringup 3dsensor.launch' -p hold --new_tab
else
    echo "Host is offline... aborting"
fi

