#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
import subprocess

def Move(vel_msg,pub):
    speed = 5
    side = 4 #Polygon side length
    vel_msg.linear.x = speed
    t0 = rospy.Time.now().to_sec()
    distance=0
    
    while(distance < side):
        pub.publish(vel_msg)
        t1=rospy.Time.now().to_sec()             
        distance = speed*(t1-t0)

    vel_msg.linear.x = 0
    pub.publish(vel_msg)

def Rotate(shape_angle,vel_msg,pub):
    angular_speed = 2
    vel_msg.angular.z = angular_speed
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < shape_angle):
        pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0
    pub.publish(vel_msg)

def Circle():
    rospy.init_node('CircleTurtle',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x=2
    vel_msg.angular.z=1.8
    
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
    
    vel_msg.linear.x=0
    vel_msg.angular.z=0
    print("\nCircle is drawn, thank you!")

def Square():
    rospy.init_node('SquareTurtle',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    count=0
    
    while(count<5):
        Move(vel_msg,pub)
        Rotate(math.pi/2,vel_msg,pub)
        count+=1
    print("\nSquare is drawn, thank you!")

def Triangle():
    rospy.init_node('TriTurtle',anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
    count=0
    
    while(count<4):
        Move(vel_msg,pub)
        Rotate(2*math.pi/3,vel_msg,pub) # 2pi/3 is the interior angle 
        count+=1
    print("\nTriangle is drawn, thank you!")

if __name__ == '__main__':
    try:
        subprocess.call(["./reset.sh"])
        print("\nWelcome to Turtle draws shape\n")
        print("-----MENU----\n")
        print("1.Circle\n2.Square\n3.Triangle\n(ctrl + c to exit)\n")
        opt = int(input("Enter option: "))
        
        if(opt==1):
            Circle()
        elif(opt==2):
            Square()
        elif(opt==3):
            Triangle()

    except rospy.ROSInterruptException:
        pass


