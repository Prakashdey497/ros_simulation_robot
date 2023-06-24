#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
 
class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher_node")
 
 
def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()