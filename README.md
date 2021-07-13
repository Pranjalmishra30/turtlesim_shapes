# Turtlesim_Draw  
A ROS package to draw shapes using [turtlesim](http://wiki.ros.org/turtlesim)  

## Install the package 
Run the following commands in your terminal to install this package.  
```
cd ~/catkin_ws/src  
git clone https://github.com/Pranjalmishra30/turtlesim_shapes.git  
cd ..  
catkin_make  
source devel/setup.bash  
```  
Run the command `chmod +x reset.h` to make the .sh file executable  

## Running the package  

* Open a new terminal window  
  
  Run the following command to source your catkin workspace   
  (**Note**: Ignore this if you have already included the source command in your .bashrc file)  
  ```
  source devel/setup.bash
  ```  
 
  Run the command to launch the turtlesim node  
  ```
  roslaunch turtlesim_shapes turtleshape.launch
  ```  

* Open a new terminal window  
  
  Run the following command to source your catkin workspace   
  (**Note**: Ignore this if you have already included the source command in your .bashrc file)  
  ```
  source devel/setup.bash
  ```  
 
  Run the command to run the draw shape node  
  ```
  rosrun turtlesim_shapes code.py
  ```  
  Follow the on-screen instructions to draw various shapes  
  
