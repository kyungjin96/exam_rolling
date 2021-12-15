#!  /usr/bin/env python3
from pickle import TRUE
import time
import rospy
from std_msgs.msg import Float64



rospy.init_node('rolling')
left_pub = rospy.Publisher('/left_arm_controller/command',Float64, queue_size=10 )
right_pub = rospy.Publisher('/right_arm_controller/command',Float64, queue_size=10 )
left_dir = 0.0
right_dir = 0.0




def stop():
    left_dir = 0.0
    right_dir = 0.0
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
    return

def gogo():
 
    left_dir = 1.0
    right_dir = 1.0
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
        
    return

def bag():
    left_dir = -1.0
    right_dir =-1.0
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
        
    return

def tornado() :
    left_dir = 1.0
    right_dir = -1.0
    return



def main():

    while True:
        z = input('전진=w, 스탑=s, 후진=x  : ' )
        if z == 'w' :
            gogo()

        if z == 's' :
            stop()
        if z == 'x' :
            bag()
   
    return


if __name__ == '__main__' :
    main()
    pass


#pub /left_arm_controller/command std_msgs/Float64 "data: 0.0" 

