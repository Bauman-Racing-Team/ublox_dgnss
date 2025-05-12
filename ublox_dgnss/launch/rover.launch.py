import launch
from launch_ros.actions import ComposableNodeContainer, Node
from launch_ros.descriptions import ComposableNode
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config = get_package_share_directory("ublox_dgnss") + "/config" + "/rover_config.yaml"

    ld = LaunchDescription(
        [
            Node(
                parameters=[config],
                package="ublox_dgnss_node",
                executable="ublox_dgnss_node",
                name="ublox_rover",
                output="screen",
                # prefix=["gdbserver localhost:3000"],
                # emulate_tty=True
            ),
        ]
    )

    return ld
