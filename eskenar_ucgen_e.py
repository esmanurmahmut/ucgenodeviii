#!/usr/bin/env python3


import rospy
from ogretici_paket.msg import EsmanurunGeometrisi
from nav_msgs.msg import Odometry
from tf import transformations
from math import radians


class GoForward:

    def forward(self,lin,ang):
        rospy.loginfo("Moving - lin : {} ang : {}".format(lin,ang))
        move_cmd = EsmanurunGeometrisi()
        move_cmd.linear.x = lin
        move_cmd.angular.z = ang
        self.cmd_vel.publish(move_cmd)

    def __init__(self):
        rospy.init_node('GoForward', anonymous=False)

        rospy.loginfo("To stop TurtleBot CTRL + C")

        rospy.on_shutdown(self.shutdown)
        rospy.Subscriber("odom", Odometry, self.odomCallback)
        self.guncel_aci = 0.0
        self.cmd_vel = rospy.Publisher('cmd_vel', EsmanurunGeometrisi, queue_size=10)
     
        r = rospy.Rate(30);
	
        while not rospy.is_shutdown():
            angle = radians(60)
            # Rotate 
            t0 = rospy.get_rostime().secs
            while(t0 + 1.04 >= rospy.get_rostime().secs):
                self.forward(0,angle)
            # Move forward at 0.3 for 5 sec
            t0 = rospy.get_rostime().secs
            while(t0 + 5 >= rospy.get_rostime().secs):
                self.forward(0.3,0)
            # Rotate
            t0 = rospy.get_rostime().secs
            while(t0 + 1.04 >= rospy.get_rostime().secs):
                self.forward(0,angle)
            # Move forward at 0.3 for 5 sec
            t0 = rospy.get_rostime().secs
            while(t0 + 5 >= rospy.get_rostime().secs):
                self.forward(0.3,0)
            t0 = rospy.get_rostime().secs
            while(t0 + 1.04 >= rospy.get_rostime().secs):
                self.forward(0,angle)
            # Move forward at 0.3 for 5 sec
            t0 = rospy.get_rostime().secs
            while(t0 + 5 >= rospy.get_rostime().secs):
                self.forward(0.3,0)
            break
            # r.sleep()
    
    def odomCallback(self, mesaj):
        self.guncel_aci = mesaj
        # print(self.guncel_aci)
        # print("--------------------")
        turtlebot_orientation_in_degrees = 60
        #convert euler to quaternion and save in new variable quat
        quat = transformations.quaternion_from_euler(0, 0, radians(turtlebot_orientation_in_degrees))

                        
        
    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(EsmanurunGeometrisi())
        # rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        move = GoForward()
	
    except:
        rospy.loginfo("GoForward node terminated.")