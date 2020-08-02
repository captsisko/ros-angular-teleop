#! /usr/bin/env python

from __future__ import print_function

from topics_lister.srv import FetchTopics, FetchTopicsResponse
import rospy
from rosapi import proxy, objectutils, params
from rosapi.srv import *

def sendTopics(request):
    # print("%s" %request)
    print("_________________________")
    # return FetchTopicsResponse( ['test1'], ['test2'] )
    # return FetchTopicsResponse( ['test1', 'test2'], ['test1', 'test2'] )
    return FetchTopicsResponse( [['topic1', 'type1'], ['topic2', 'type2']] )
    

    # args should be ['topics', 'types'] args are(['test1', 'test2'],)

    # ['/turtle1/color_sensor', 'turtlesim/Color'],
    # ['/client_count', 'std_msgs/Int32'],
    # ['/rosout', 'rosgraph_msgs/Log'],
    
    # topics, types = proxy.get_topics_and_types(rosapi.glob_helper.topics_glob)
    # return FetchTopicsResponse(topics, types)

# def topics_server():
rospy.init_node('fetch_topics_server')
# rospy.Service('/rosapi/topics', Topics, sendTopics)
s = rospy.Service('fetch_topics', FetchTopics, sendTopics)
print ("Serving topics ...")
rospy.spin()

# if __name__ == "__main__":
#     topics_server()