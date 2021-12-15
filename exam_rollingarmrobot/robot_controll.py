import rospy
import cv2
from sensor_msgs.msg import Image

from cv_bridge import CvBridge
bridge = CvBridge()
def callback(data):
    cv2_img = bridge.imgmsg_to_cv2(data, 'bgr8')
    cv2.imshow('callback',cv2_img)
    key = cv2.waitKey(1)
    if key == ord('w'):
        g

    pass


rospy.init_node('img_raw_opencv')
rospy.Subscriber('/camera/image_raw', Image, callback)
rospy.spin()