# challenge_visualization

Setup (only run once):

```bash
# this may be installed on your drone already:
$ sudo apt-get install ros-kinetic-web-video-server

$ cd ~/bwsi-uav/catkin_ws/src/
$ git clone https://github.com/BWSI-UAV/challenge_visualization
```

# Running:

You can either:

1. Add this node to your launch file
2. `roslaunch challenge_visualization converter.launch`

In Chrome, navigate to http://teamname.beaver.works:8080

Select the `visualiztion/converter` image topic in the browser.
