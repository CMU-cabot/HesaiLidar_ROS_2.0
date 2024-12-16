from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        Node(namespace='hesai_ros_driver', package='hesai_ros_driver', executable='hesai_ros_driver_node', output='screen'),
    ])
