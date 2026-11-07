# ROS 2 Mini Communication System

A simple ROS 2 communication system developed using Python and `rclpy`.

## Project Overview

This project demonstrates basic publisher-subscriber communication in ROS 2 using two nodes.

## Features

- Random number generation
- Publisher and subscriber communication
- Number doubling
- Custom QoS configuration
- ROS 2 topic monitoring
- Rosbag recording and playback

## Nodes

**1. number_publisher**
- Generates random integers between 1 and 1000.
- Publishes messages to `/number` at 2 Hz.

**2. number_doubler**
- Subscribes to `/number`.
- Multiplies received values by 2.
- Publishes results to `/number_doubled`.

## Topics

| Topic | Message Type | Description |
|---|---|---|
| `/number` | `std_msgs/Int32` | Random numbers |
| `/number_doubled` | `std_msgs/Int32` | Doubled numbers |

## QoS Settings

- Reliability: RELIABLE
- Durability: TRANSIENT_LOCAL
- Queue Depth: 10

## Requirements

- ROS 2 Humble
- Python 3
- `rclpy`
- `std_msgs`

## Build and Run

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

Run the publisher:

```bash
ros2 run mini_haberlesme number_publisher
```

Run the doubler in another terminal:

```bash
ros2 run mini_haberlesme number_doubler
```

## Monitoring

```bash
ros2 topic list
ros2 topic echo /number
ros2 topic hz /number
ros2 topic info /number --verbose
```

## Rosbag

Record topics:

```bash
ros2 bag record /number /number_doubled
```

Inspect the recording:

```bash
ros2 bag info BAG_FOLDER
```

Play the recording:

```bash
ros2 bag play BAG_FOLDER
```

## Author
Şeyma Güvel

Software Engineering Student

Developed as a ROS 2 learning project.
