#!/usr/bin/env python3
# coding:utf-8

import rospy
from cmd_video.srv import cmd, cmdRequest, cmdResponse

def if_success(request):
    if not isinstance(request, cmdRequest):
        print("Error request")
        return
    else:
        print(f"Get commond x={request.x}, y={request.y}, z={request.z}, yaw={request.yaw}")
        flag = 0
    return cmdResponse(flag)

def cmd_server():
    rospy.init_node('server_node')
    service_name = '/serHostFBLR'
    server = rospy.Service(service_name, cmd, callback=if_success)
    print("Ready to get the fly cmd...")
    rospy.spin()

if __name__ == '__main__':
    cmd_server()