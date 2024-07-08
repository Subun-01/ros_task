## So what is Holonomic Drive?

An object in the physical “3D” space we live in has 6 Degreed of Freedom.
3 translations, 3 rotations.

An object on a “2D” plane has 3 Degreed of freedom:
2 translations and 1 rotation.

In our convention, it will be translation in the X and Y axis and rotation about the Z axis.

Ground vehicles live on a plane.
The popular differential drive robot has a Non Holonomic CONSTRAINT. That doesn’t allow the robot to translate in one of the axis (say X). This is a constraint on velocity and NOT a constraint on position. So although a differential drive CAN parallel park it has to make many complex manoeuvres to achieve it. While a holonomic drive (ex: Omni wheel robot) can simply translate in that direction (X) since it has no such constraint in that direction.

I.E. The ground vehicle can directly control velocities in ALL the 3 Degrees of Freedom possible.
I.E. Control [v_x, v_y, w] linear velocity in X-Y and Omega: angular velocity in the Z axis. (Unlike only two, [v, w] (or [v_y, w] in our convention) for a differential drive robot.)

The above block of explanation might now give you some clarity on what is holonomic drive.

Enough chit-chat, let’s get down to business!


## The Task
So continuing from where we left off in Step1. We now have a launch file which opens gazebo, empty world and spawns the robot.

If you do that and then do rostopic list, you should find two topic of interest:

/cmd_vel
/odom
which are defined in the urdf file, gazebo plugin.

Now we shall create a rclpy node: controller.py that will

subscribe to /odom and
publish to /cmd_vel


## Now let’s start writing the controller.py file.

The content of the comment in boilerplate code is very important so let’s repeat it here:

Find error (in x, y and theta) in global frame

the /odom topic is giving present pose of the robot in global frame
the desired pose is declared above and defined by you in global frame therefore calculate error in global frame
Calculate error in body frame

Controller outputs robot velocity in robot_body frame, i.e. velocity are define is in x, y of the robot frame,
Notice: the direction of z axis says the same in global and body frame therefore the errors will have have to be calculated in body frame.
Finally implement P controllers to react to the error in robot_body frame with velocities in x, y and theta in robot_body frame: [v_x, v_y, w]

This is probably the crux of Task 2B
Please note this is just the approach we took, there may be other approaches that you may come up with.
Feel absolutely free to go ahead with that approach.

### The objective is simple
Make the robot go to desired [x_d, y_d, theta_d] 
Thats it!

If the robot goes to the desired goal pose (defined by you), Congratulations! You have achieved a major milestone!

Once you have entered a list of goal poses, make necessary changes to the control loop to:

go-to-goal-pose of a certain index (index = 0 at start)
identify if the goal has been reached (write an if condition)
stabilise/stay at the goal pose for at least 1 second
increment index if index < length of the list.
repeat
That’s it!

If the robot goes to the sequence of desired goal poses one after other (defined by you), Congratulations you are almost done with Task 2B!🥳

