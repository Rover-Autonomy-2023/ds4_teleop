#!/usr/bin/env/python3

# ROS Client libraries
import rclpy
from rclpy.node import Node

# ROS message types
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class DriveTeleop(Node):
    def __init__(self):
        super().__init__("drive_teleop")

        self.joy_sub_ = self.create_subscription(Joy, '/joy', self.joy_to_twist, 10)
        self.twist_pub_ = self.create_publisher(Twist, 'teleop/cmd_vel', 10)

        self.declare_parameter("max_vel")

    @property
    def max_vel(self) -> float:
        """ Get real-time parameter value of the maximum velocity in m/s

        Returns:
            float: latest parameter value of the maximum velocity
        """
        return self.get_parameter("max_vel").value

    def joy_to_twist(self, joy_msg: Joy) -> None:
        twist_msg = Twist()

        # TODO: Add logic to extract linear and angular velocities
        twist_msg.linear.x = 0 *  self.max_vel
        twist_msg.angular.z = 0

        self.twist_pub_.publish(twist_msg)


def main(args=None):
    rclpy.init(args=args)
    node = DriveTeleop()

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
