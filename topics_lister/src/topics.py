#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from topics_lister.msg import Topics

rospy.init_node('topics')

publisher = rospy.Publisher('/all_topics', Topics, queue_size=1)
# publisher = rospy.Publisher('/all_topics', msg._type, queue_size=1)
rate = rospy.Rate(3) # 3hz

topic_msg = Topics()
index = 0

while not rospy.is_shutdown():
	#publisher.publish('Hi')
	# topics = rospy.get_published_topics()
	# topics = dict(rospy.get_published_topics()).keys()
	topics = rospy.get_published_topics()

	# len(topics)
	# for topic in topics:
	# 	print topic
	i = 0
	test = len(topics)
	while i < test:
		print topics[i]
		i += 1

	# index += 1
	# publisher.publish( topics )
	rate.sleep()
