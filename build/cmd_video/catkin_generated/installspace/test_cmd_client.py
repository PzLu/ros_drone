#!/usr/bin/env python3
# coding:utf-8

import rospy
from cmd_video.srv import cmd, cmdRequest, cmdResponse

def cmd_client(x, y, z, yaw):
    rospy.init_node('client_node')

    rospy.wait_for_service('/serHostFBLR')
    try:
        client = rospy.ServiceProxy('serHostFBLR', cmd)

        # send request to server
        request = cmdRequest()
        request.x = x
        request.y = y
        request.z = z
        request.yaw = yaw

        response = client.call(request)

        if isinstance(response, cmdResponse):
            print("Send commond successfully")

    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")


if __name__== "__main__":
    xx, yy, zz, yawy = map(int,input().split(' '))
    cmd_client(xx, yy, zz, yawy)
