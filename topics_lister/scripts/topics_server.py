#! /usr/bin/env python

from __future__ import print_function

from topics_lister.srv import FetchTopics, FetchTopicsResponse
import rospy
from topics_lister.msg import Topic

def sendTopics(request):
    # print("%s" %request)
    # print("_________________________")

    msg_topic_1 = Topic('/turtle1/color_sensor', 'turtlesim/Color')
    # msg_topic_1 = Topic(name = '/turtle1/color_sensor', type =  'turtlesim/Color')
    # msg_topic_3 = Topic(name = '/rosout', type = 'rosgraph_msgs/Log')

    response = FetchTopicsResponse()
    # response.topics = [msg_topic_1 , msg_topic_2 , msg_topic_3 ]
    response.topics = [msg_topic_1]

    return response

def topics_server():
    rospy.init_node('fetch_topics_server')
    s = rospy.Service('fetch_topics', FetchTopics, sendTopics)
    print ("Serving topics ...")
    rospy.spin()

if __name__ == "__main__":
    topics_server()