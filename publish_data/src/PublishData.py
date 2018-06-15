#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage,PointCloud
from geometry_msgs.msg import Twist
import pandas as pd
import time
import io
import matplotlib.image as mpimg
import numpy

def image(msg):
	global image_array
	image_file = io.BytesIO(msg.data)
	image_array = mpimg.imread(image_file,format='jpg')
	image_array=image_array.reshape(1,240,352,3)
	#print(image_array.shape)
	#print('new\n')
	return



def vel(msg):
	global angular
	print(msg)
	return


def sonar(msg):
	global sonar_list
	global angular
	df = pd.DataFrame(columns=['points'])
	try:
		df['points']=msg.points
		for i in range(16):
			df['points'][i]=df['points'][i].x**2 + df['points'][i].y**2
		sonar_list = (df['points']**.5).tolist()
		sonar_list.append(angular)
		s=numpy.array(sonar_list)
		s=s.reshape(1,17)
		print s.shape
	except SystemError as a:
		print('error in code' + a)
	
	return





def node():
	rospy.init_node('PublishData',anonymous=True)
	
	rospy.Subscriber('/image_raw/compressed',CompressedImage,image)
	rospy.Subscriber('/RosAria/sonar',PointCloud,sonar)
	rospy.Subscriber('/cmd_vel',Twist,vel)


if (__name__=="__main__"):
	angular = 0.00000000
	sonar_list = []
	image_array = numpy.empty([240,352,3])
	node()
	rospy.spin()
