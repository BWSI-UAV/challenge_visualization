#!/usr/bin/env python
import numpy as np
import rospy
import cv2
import threading
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge, CvBridgeError

class Imagemerge:
    def __init__(self):
        # Create node with name 'merge'
        rospy.init_node('merge')

        # A subscriber to the topic '/aero_downward_camera/image'. self.image_sub_cb is called when a message is recieved
        self.forward_color_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.forward_color_sub_cb)
       # self.forward_depth_sub = rospy.Subscriber('/camera/depth/image_raw', Image, self.forward_depth_sub_cb)
	self.downward_raw_sub = rospy.Subscriber('/aero_downward_camera/image',Image,self.downward_raw_sub_cb)
	self.downward_line_sub = rospy.Subscriber('/line/detector_image',Image, self.downward_line_sub_cb)
        # create local variables for the drone
        self.master_image = np.zeros((360,360, 3), np.uint8)
	self.sub_image = np.zeros((360,480,3),np.uint16)
        # A publisher which will publish an image annotated with the detected line to the topic 'line/detector_image'
        self.converter_image_pub = rospy.Publisher('/visualization/converter_image', Image, queue_size=1)

        # Initialize instance of CvBridge to convert images between OpenCV images and ROS images
        self.bridge = CvBridge()
    def downward_line_sub_cb(self,img):
	converted_img = self.bridge.imgmsg_to_cv2(img, "8UC3")
	self.master_image[180:360, 180:360,:] = cv2.resize(converted_img, (180,180))
  
    def forward_color_sub_cb(self, img):
        """ Add the forward color image to a portion of the master image. """
        converted_img = self.bridge.imgmsg_to_cv2(img, "8UC3") # convert from ROS to cv2 images.
        self.master_image[:180, :360, :] = cv2.resize(converted_img, (360,180)) # downsize the image

    #def forward_depth_sub_cb(self, img):
     #   "Add the forward depth camera to a portion of the master image."
      #  converted_img = self.bridge.imgmsg_to_cv2(img, "16UC1") # convert from ROS to cv2 images.
#	converted2_img = np.floor_divide(converted_img,5)
#	inter_img = np.array(converted2_img, dtype=np.uint8) 
#	fin_img = cv2.resize(inter_img,(250,250))
 #       self.master_image[:250, 250:500, :] = cv2.applyColorMap(fin_img, cv2.COLORMAP_JET)
    def downward_raw_sub_cb(self, img):
	converted_img = self.bridge.imgmsg_to_cv2(img,"8UC1")
	reconverted_img = cv2.cvtColor(converted_img, cv2.COLOR_GRAY2BGR)
	self.master_image[180:360, :180,:] = cv2.resize(reconverted_img, (180,180))
	

    def stream_images(self, hz=12):
        """ Publish the master images at a regular rate """
        rate = rospy.Rate(hz) # only publish infrequently to save on CPU cycles.
        while not rospy.is_shutdown():
            col_msg = self.bridge.cv2_to_imgmsg(self.master_image, "rgb8")
            self.converter_image_pub.publish(col_msg)
            rate.sleep()



if __name__ == '__main__':
    merge = Imagemerge()
    rospy.loginfo("Image convert initialized")
    merge.stream_images()
