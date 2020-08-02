#!/usr/bin/env python

import rospy
import sys
from basics.srv import WordCount

rospy.init_node('service_client')

rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count', WordCount)

words = ' ' . join(sys.argv[1:])

word_count = word_counter(words)

print words, '->', word_count.count