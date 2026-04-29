# ROS2 Latency & QoS Evaluator

**Author:** Koushik Samudrala  
**Environment:** Ubuntu 22.04 LTS / ROS2 Humble

## Overview
This project is a simulation tool designed to evaluate network communication parameters—specifically latency and packet loss—within a ROS2 environment. It was built to demonstrate an understanding of **Quality of Service (QoS)** profiles and their critical role in ensuring reliable, real-time data transmission for cooperative humanoid robotics and sensor fusion.

The simulation consists of two nodes:
1.  **Ping Node (Publisher):** Generates and transmits a timestamp.
2.  **Pong Node (Subscriber):** Receives the timestamp, compares it to the current time, and calculates the network latency.

## Key Concepts Demonstrated
   *   **ROS2 Communication Architecture:** Utilizing Publisher/Subscriber models for continuous sensor data streams.
   *   **Quality of Service (QoS):** Comparing `RELIABLE` vs. `BEST_EFFORT` policies under constrained network conditions.
   *   **Network Diagnostics:** Analyzing latency spikes and packet loss scenarios critical for robotic control loops.

## Setup and Installation

### Prerequisites
   *   Ubuntu 22.04
   *   ROS2 Humble installed

### Build Instructions
1. Clone this repository into the `src` folder of a new ROS2 workspace:
   ```bash
       mkdir -p ~/latency_ws/src
       cd ~/latency_ws/src
       git clone [https://github.com/KoushikSamudrala/ros2_latency_evaluator.git](https://github.com/KoushikSamudrala/ros2_latency_evaluator.git)
   ```
2. Navigate to the root of the workspace and build:
       
 ```bash
       cd ~/latency_ws
       colcon build
       source install/setup.bash
  ```

## Running the Simulation

You will need two terminals. Ensure you source your workspace (`source install/setup.bash`) in both.

   **Terminal 1 (Publisher):**
    
```bash
    ros2 run latency_evaluator ping_node
    ```

    **Terminal 2 (Subscriber):**
    ```bash
    ros2 run latency_evaluator pong_node
```

## Simulating Network Degradation (Linux 'tc')
To truly test the QoS profiles, simulate a degraded network (e.g., 20ms delay, 5% packet loss) on your local loopback interface:

```bash
    sudo tc qdisc add dev lo root netem delay 20ms loss 5%
```
 *(Run `sudo tc qdisc del dev lo root` to reset network conditions afterwards).*
Compare the latency outputs when running the nodes with a `RELIABLE` QoS profile versus a `BEST_EFFORT` profile.
