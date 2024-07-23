#!/usr/bin/env python3

################### IMPORT MODULES #######################
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Bool
import cv2
import numpy as np

############################################################


class VisualizationNode(Node):

    def __init__(self):
        super().__init__("visualization_node")

        ######### Required variables ############
        self.viz_img = np.full((500, 500, 3), (255, 255, 255), dtype=np.uint8)
        self.drawing_status = False
        self.bridge = CvBridge()
        self.camera_image = self.viz_img
        self.bot_pose = None
        #########################################

        ######### Publishers & Subscribers ######
        self.pen_down_subscription_1 = self.create_subscription(
            Bool, "/draw", self.drawingStatusCallback, 10
        )
        self.sub_image = self.create_subscription(
            Image, "/camera/image_raw", self.imageCallback, 10
        )
        self.pose_subscription_1 = self.create_subscription(
            Pose2D, "/bot_pose", self.botPoseCallback, 10
        )
        ##########################################

    ######### Callback functions ###############
    def imageCallback(self, msg):
        # convert ROS image to opencv image
        self.camera_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

    def drawingStatusCallback(self, msg: Bool):
        self.drawing_status = msg.data

    def botPoseCallback(self, msg: Pose2D):
        if self.drawing_status:
            self.bot_pose = (int(msg.x), int(msg.y))

    ##############################################


def main(args=None):

    rclpy.init(args=args)

    viz_node = VisualizationNode()
    while rclpy.ok():
        # Draw the path
        if viz_node.bot_pose:
            viz_node.viz_img = cv2.line(
                viz_node.viz_img,
                viz_node.bot_pose,
                viz_node.bot_pose,
                (50, 100, 200),
                3,
            )

        cv2.imshow("Visualization_image", viz_node.viz_img)
        cv2.imshow("camera_view", viz_node.camera_image)
        cv2.waitKey(1)
        rclpy.spin_once(viz_node)

    viz_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()


