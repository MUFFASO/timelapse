#!/usr/bin/python
import os
import time
import sys

frames = 30
interval = 5

print('\x1b[6;30;42m' + '---> Comienza el script...' + '\x1b[0m')
os.system("mkdir ./tmp-timelapse/")
while frames > 0:   
    print('\x1b[6;30;42m' + '---> Frames #'+str(frames)+' to finish' + '\x1b[0m')
    os.system("fswebcam -i 0 -d /dev/video0 -r 640x480 --set sharpness=8 --skip 10 --no-banner ./tmp-timelapse/%y%m%d_%H%M%S.jpg")
    frames = frames-1
    time.sleep(interval)
print('\x1b[6;30;42m' + "\e[1m\e[7m---> Convirtiendo..." + '\x1b[0m')
os.system("ffmpeg -r 15 -pattern_type glob -i './tmp-timelapse/*.jpg' -s 640:480 -c:v h264 -strftime 1 './timelapse.mp4'")
print('\x1b[6;30;42m' + '---> Eliminando imgs...' + '\x1b[0m')
os.system("rm -r ./tmp-timelapse/")
print('\x1b[6;30;42m' + '---> Fin' + '\x1b[0m')
sys.exit()
