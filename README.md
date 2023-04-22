# Object Detection Program
This Python program captures live video from a camera and performs object detection using cvlib library, a high-level computer vision library built on top of OpenCV. Detected objects are displayed with bounding boxes and labels in real-time.

# Prerequisites
Before running the program, make sure you have the following dependencies installed:

- Python 3.x  

- OpenCV (cv2) library  

- cvlib library  

- cvlib's object_detection module  

You can install the required libraries using pip, for example:  


- css  

- Copy code  

- pip install opencv-python  

- pip install cvlib  

- pip install cvlib[object_detection]  

# Usage  

Clone or download the repository to your local machine.  

Connect a camera to your machine or use the built-in camera of your device.  


Run the object_detection.py script using Python 3.x:  

Copy code  

python object_detection.py  

The program will open a window titled "Object Detection" showing the live video feed from the camera. Detected objects will be displayed with bounding boxes and labels.  

Press the spacebar to stop the program and close the camera window.  

The program will print a sentence describing the detected objects based on their labels.  

# Credits
This program uses the cvlib library, which is a high-level computer vision library built on top of OpenCV. For more information about cvlib, visit: https://github.com/arunponnusamy/cvlib  
The development of this object detection program was based on learning from online educational resources, including the video tutorial available at https://www.youtube.com/watch?v=V62M9d8QkYM, and further customized to suit specific requirements.  


# License
This program is open-source and released under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

# Disclaimer
This program is provided as-is, without any warranties or guarantees. The authors are not responsible for any misuse, damage, or harm caused by the program. Use it at your own risk. Always be cautious when working with live video feeds and cameras.
