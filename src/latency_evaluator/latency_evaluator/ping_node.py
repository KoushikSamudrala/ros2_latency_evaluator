import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
import time

class PingNode(Node):
    def __init__(self):
        super().__init__('ping_node')

        # --- QOS SETUP ---
        # Here we define the QoS profile.
        # Try changing RELIABLE to BEST_EFFORT later to see the difference.
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.publisher_ = self.create_publisher(String, 'latency_test_topic', qos_profile)

        # Publish 10 times a second (10 Hz)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Ping Node has been started.')

    def timer_callback(self):
        msg = String()
        # Get current time in seconds (as a float)
        current_time = time.time()
        # Put the timestamp into the string message
        msg.data = str(current_time)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing timestamp: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    ping_node = PingNode()
    rclpy.spin(ping_node)
    ping_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
