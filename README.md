# Timelapse Video
- Simple time lapse video using fswebcam, python and ffmpeg

- This script creates a video with pics taken from webcam device


## Requirements
- python
- fswebcam
- ffmpeg

Tested on **Raspbian** under **Raspberry PI 3B+** with generic usb webcam

## Usage
>timelapse.py --frames [frames] --interval [interval in seconds] --device [device] --sharpness [0 to 11]


**Example**

    timelapse.py --frames 60 --interval 5 --device /dev/video0 --sharpness 8

**Defaults**
- frames: 60
- interval: 5
- device: /dev/video0
- sharpness: 8
