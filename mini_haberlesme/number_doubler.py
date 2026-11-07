#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

class NumberDoublerNode(Node):

    def __init__(self):
        super().__init__("number_doubler")
        self.get_logger().info("Number doubler has been started")


        qos_profile = QoSProfile(
            depth = 10,
            reliability = ReliabilityPolicy.RELIABLE,
            durability = DurabilityPolicy.TRANSIENT_LOCAL
        )
        
        self.publisher = self.create_publisher(
            Int32,
            '/number_doubled',
            qos_profile

        )

        self.subscription = self.create_subscription(
            Int32,
            '/number',
            self.listener_callback,
            qos_profile
        )

    def listener_callback(self,msg):
        doubled_msg = Int32()
        doubled_msg.data = msg.data*2

        self.publisher.publish(doubled_msg)

        self.get_logger().info(f'Received: {msg.data}, Published: {doubled_msg.data}')

def main(args=None):
    rclpy.init(args = args)
    node = NumberDoublerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__name__':
    main()




