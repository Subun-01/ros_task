# Visualization Node Instructions

## Overview
Review the provided code to understand its functionality, as this will assist you in completing the task.

## Important Instructions
1. **Do not modify the code.**
2. **Run this code before executing any bot control scripts.**
3. Once you achieve the correct drawing as specified, **save the resulting visualization_image for future submission.**

## Code Explanation

### Import Modules
The following modules are imported:
- `rclpy`: The ROS 2 Python client library.
- `Node`: Base class for creating ROS 2 nodes.
- `Image`: Message type for camera images.
- `CvBridge`: Library to convert ROS image messages to OpenCV images.
- `Pose2D`: Message type for 2D poses.
- `Bool`: Standard boolean message type.
- `cv2`: OpenCV library.
- `numpy`: Library for numerical operations.

### VisualizationNode Class
The `VisualizationNode` class inherits from `Node` and includes:
- **Variables:**
  - `viz_img`: A blank 500x500 white image for visualization.
  - `drawing_status`: A boolean indicating if drawing is enabled.
  - `bridge`: An instance of `CvBridge` for image conversion.
  - `camera_image`: Stores the latest camera image.
  - `bot_pose`: Stores the current position of the robot.
  
- **Publishers & Subscribers:**
  - Subscribes to the `/draw` topic to get drawing status.
  - Subscribes to the `/camera/image_raw` topic to get camera images.
  - Subscribes to the `/bot_pose` topic to get the robot's position.

- **Callback Functions:**
  - `imageCallback`: Converts ROS image messages to OpenCV images.
  - `drawingStatusCallback`: Updates the drawing status.
  - `botPoseCallback`: Updates the robot's position if drawing is enabled.

### Main Function
- Initializes the ROS 2 system.
- Creates an instance of `VisualizationNode`.
- In a loop, it:
  - Draws the path on `viz_img` if `bot_pose` is available.
  - Displays the visualization and camera images using OpenCV.
  - Spins the node once to handle callbacks.


## Usage
1. Ensure you have the necessary dependencies installed.
2. Save the provided script as `visualization_node.py`.
3. Run the script using the following command:

   ```sh
   python3 visualization_node.py