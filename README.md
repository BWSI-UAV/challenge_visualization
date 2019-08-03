### challenge_visualization

# NEW SETUP INSTRUCTIONS (August 3 5PM)

Setup (only run once):

```
# STEP 1: get rid of this if you have installed it
sudo apt-get remove ros-kinetic-web-video-server

# STEP 2 clone this repo into your catkin workspace
# *****************************************************
# ** NOTE: SKIP STEP 2 if you already have it cloned **
# *****************************************************
cd ~/bwsi-uav/catkin_ws/src/
git clone https://github.com/BWSI-UAV/challenge_visualization

# STEP 3: update challenge_visualization
cd ~/bwsi-uav/catkin_ws/src/challenge_visualization
git pull

# STEP 4: clone the latest version of web_video_server and build it
cd ~/bwsi-uav/catkin_ws/src/
git clone https://github.com/RobotWebTools/web_video_server

# STEP 5: build the changes to your catkin_ws 
cd ~/bwsi-uav/catkin_ws/
catkin_make
```

Add the following to your challenge launch file somewhere inside the <launch> tag
  ```
  <!-- Launch nodes for video streaming -->
  <node pkg="challenge_visualization" name="merge" type="merge.py"/>
  <node pkg="web_video_server" name="video_server" type="web_video_server"/>
  ```

# Running:

After running your final challenge launch file with the added merge and web_video_server nodes open a web browser and navigate to http://teamname.beaver.works:8080

Select the `visualiztion/converter` image topic in the browser.

`Ctrl` + `+` will increase the video size

# Critical Note:

Only **one** team member should open the video feed in their browser - each open video feed takes 10%-20% of the available CPU. For the final challenge, we will have one feed open on large monitors for the audience to view.
