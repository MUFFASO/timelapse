# Timelapse
Simple time lapse video with fswebcam, python and ffmpeg

This script creates a video with pics taken from webcam device

1- Clone

2- Run

timelapse.py --frames [frames] --interval [interval in seconds] --device [device] --sharpness [0 to 11]


ex: timelapse.py --frames 60 --interval 5 --device /dev/video0 --sharpness 8


Defaults
frames: 60
interval: 5
device: /dev/video0
sharpness: 8
