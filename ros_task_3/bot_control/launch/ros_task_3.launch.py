''' 
*****************************************************************************************
*
*        =============================================
*                  Cyborg ROS Task-3
*        =============================================
*
*
*  Filename:			ros_task_3.launch.py
*  Description:         Use this file to spawn bot.
*  Created:				16/07/2023
*  Last Modified:	    04/07/2024
*  Modified by:         Soumitra Naik
*  Author:				e-Yantra Team (Srivenkateshwar)
*  
*****************************************************************************************
'''

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.actions import IncludeLaunchDescription ,DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution,LaunchConfiguration, PythonExpression
import os
from ament_index_python.packages import get_package_share_directory,get_package_prefix


def generate_launch_description():
    share_dir = get_package_share_directory('bot_control')
    pkg_sim_world = get_package_share_directory('task_arena')
    pkg_sim_bot = get_package_share_directory('mini_bot')


     
    world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_sim_world, 'launch', 'world.launch.py'),
        )
    )
    spwan_bot=IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_sim_bot, 'launch', 'spawn_bot.launch.py'),
        )
    )
    return LaunchDescription([
        world,
        spwan_bot
  
        
        ])
