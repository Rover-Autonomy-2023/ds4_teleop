#!/usr/bin/env/python3

from pyPS4Controller.controller import Controller

# ROS Client libraries
import rclpy
from rclpy.node import Node

# ROS Joystick message types
from sensor_msgs.msg import Joy, JoyFeedback

class DS4InputPublisher(Node):
    def __init__(self):
        super().__init__("ds4_input_publisher")
        self.joy_pub_ = self.create_publisher(Joy, '/joy', 10)

    # TODO: define callback to read events and publish

def main(args=None):
    rclpy.init(args=args)
    node = DS4InputPublisher()

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
