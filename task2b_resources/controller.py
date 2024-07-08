import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import time
import math
from tf_transformations import euler_from_quaternion

class Task2BController(Node):

   def __init__(self):
        super().__init__('task2b_controller')

        # Initialze Publisher and Subscriber
        # We'll leave this for you to figure out the syntax for
        # initialising publisher and subscriber of cmd_vel and odom respectively

        # Declare a Twist message
        self.vel = Twist()
        # Initialise the required variables to 0

        # For maintaining control loop rate.
        self.rate = self.create_rate(100)
        # Initialise variables that may be needed for the control loop
        # For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
        # and also Kp values for the P Controller
        

   def main(args=None):
    rclpy.init(args=args)

    # Create an instance of the EbotController class
    mini_controller = Task2BController()

    # Send an initial request with the index from ebot_controller.index
    mini_controller.send_request(mini_controller.index)

    # Main loop
    while rclpy.ok():

        # Check if the service call is done
        if : ##provide an if logic for iterating the number of indexes required to traverse
            
            #########           GOAL POSE             #########
            ##write the logic to assign goal pose
            x_goal      = 
            y_goal      = 
            theta_goal  = 
            ####################################################

            # Find error (in x, y and theta) in global frame
            # the /odom topic is giving pose of the robot in global frame
            # the desired pose is declared above and defined by you in global frame
            # therefore calculate error in global frame

            # (Calculate error in body frame)
            # But for Controller outputs robot velocity in robot_body frame, 
            # i.e. velocity are define is in x, y of the robot frame, 
            # Notice: the direction of z axis says the same in global and body frame
            # therefore the errors will have have to be calculated in body frame.
            # 
            # This is probably the crux of Task 2, figure this out and rest should be fine.

            # Finally implement a P controller 
            # to react to the error with velocities in x, y and theta.

            # Safety Check
            # make sure the velocities are within a range.
            # for now since we are in a simulator and we are not dealing with actual physical limits on the system 
            # we may get away with skipping this step. But it will be very necessary in the long run.


            #If Condition is up to you
            
            mini_controller.index += 1


        # Spin once to process callbacks
        rclpy.spin_once(mini_controller)

    # Destroy the node and shut down ROS
    mini_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
