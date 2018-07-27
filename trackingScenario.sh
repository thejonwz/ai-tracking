#!/bin/bash

# move car
# make sure BLDCtool is the last focused window
python ~/moveCar.py forw 0.5

# let the python script get the images for 25 seconds
sleep 10s

# kill the python process, freeing gpu
killall -9 python

# train model for tello

######################
# set up the kill
./killTello.sh &
######################

# launch tello and let it do its thing
cd /home/nvidia/swx/goStuff/telloGoVideo/
./telloGoVideo

./telloGoVideo
