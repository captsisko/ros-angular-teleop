#! /usr/bin/env python

from __future__ import print_function
import sys
import rospy
# import topics_lister.srv import *
from topics_lister.srv import FetchTopics, FetchTopicsRequest, FetchTopicsResponse

rospy.init_node('topics_client')

def topics():
    rospy.wait_for_service('fetch_topics')
    try:
        fetch_topics = rospy.ServiceProxy('fetch_topics', FetchTopics)
        print(fetch_topics)
        response = fetch_topics()
        # service.call('sendTopics')
        return response.topics
    except rospy.ServiceException as ex:
        print("Service call exception: %s"%ex)

if __name__ == "__main__":
    topics()