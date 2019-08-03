# challenge_visualization

Setup (only run once):

```
# this may be installed on your drone already:
$ sudo apt-get install ros-kinetic-web-video-server

# clone this repo into your catkin workspace
$ cd ~/bwsi-uav/catkin_ws/src/
$ git clone https://github.com/BWSI-UAV/challenge_visualization

# make catkin now that you have a new package
$ cd ~/bwsi-uav/catkin_ws/src/
$ catkin_make
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
