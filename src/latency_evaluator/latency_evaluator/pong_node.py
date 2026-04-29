import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
import time

class PongNode(Node):
    def __init__(self):
        super().__init__('pong_node')

        # --- QOS SETUP ---
        # The Subscriber MUST have a compatible QoS profile with the Publisher.
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT, # Change this when you change the publisher
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.subscription = self.create_subscription(
            String,
            'latency_test_topic',
            self.listener_callback,
            qos_profile)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Pong Node has been started, listening for pings...')

        # List to store latency values for analysis later
        self.latencies = []

    def listener_callback(self, msg):
        receive_time = time.time()
        send_time = float(msg.data)

        # Calculate latency in milliseconds
        latency_ms = (receive_time - send_time) * 1000.0

        self.latencies.append(latency_ms)
        self.get_logger().info(f'Received message. Latency: {latency_ms:.2f} ms')

        # For analysis, you could calculate the average every 100 messages:
        if len(self.latencies) % 100 == 0:
            avg_latency = sum(self.latencies) / len(self.latencies)
            self.get_logger().info(f'--- Average Latency over {len(self.latencies)} messages: {avg_latency:.2f} ms ---')

def main(args=None):
    rclpy.init(args=args)
    pong_node = PongNode()
    rclpy.spin(pong_node)
    pong_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
