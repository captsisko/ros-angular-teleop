#! /usr/bin/env python

from __future__ import print_function
import sys
import rospy
# import topics_lister.srv import *
from topics_lister.srv import FetchTopics, FetchTopicsRequest, FetchTopicsResponse

rospy.init_node('topics_client')
rospy.wait_for_service('fetch_topics')

service = rospy.ServiceProxy('fetch_topics', FetchTopics)
print (service)

# print ('RESULT: ', service(0).values)

# def topics_client():
#     rospy.wait_for_service('fetch_topics')
#     try:
#         rospy.ServiceProxy('fetch_topics')
#     except expression as identifier:
#         print("Topics-Server failed to respond")

# def usage():
#     return "%s " %sys.argv[0]

# if __name__ == "__main__":
#     if len(sys.argv) == 3:
#         x = int(sys.argv[1])
#         y = int(sys.argv[2])
#     else:
#         print(usage)
#         sys.exit()
        
