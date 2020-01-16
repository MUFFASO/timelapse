#!/usr/bin/python
import os
import time
import sys

frames = 60
interval = 5
device = "/dev/video0"
sharpness = 8

if("--frames" in  sys.argv):
    frames = sys.argv[sys.argv.index("--frames") + 1]        
if("--interval" in  sys.argv):
    interval = sys.argv[sys.argv.index("--interval") + 1]        
if("--device" in  sys.argv):
    device = sys.argv[sys.argv.index("--device") + 1]        
if("--sharpness" in  sys.argv):
    sharpness = sys.argv[sys.argv.index("--sharpness") + 1]        

print('\x1b[6;30;42m' + '---> Comienza el script...' + '\x1b[0m')
os.system("mkdir ./tmp-timelapse/")
while frames > 0:   
    print('\x1b[6;30;42m' + '---> '+str(frames)+' frames to finish' + '\x1b[0m')
    os.system("fswebcam -i 0 -d "+device+" -r 640x480 --set sharpness="+str(sharpness)+" --skip 10 --no-banner ./tmp-timelapse/%y%m%d_%H%M%S.jpg")
    frames = int(frames)-1
    time.sleep(int(interval))
print('\x1b[6;30;42m' + "\e[1m\e[7m---> Convirtiendo..." + '\x1b[0m')
os.system("ffmpeg -r 15 -pattern_type glob -i './tmp-timelapse/*.jpg' -s 640:480 -c:v h264 -strftime 1 './timelapse.mp4'")
print('\x1b[6;30;42m' + '---> Eliminando imgs...' + '\x1b[0m')
os.system("rm -r ./tmp-timelapse/")
print('\x1b[6;30;42m' + '---> Fin' + '\x1b[0m')
print('\x1b[6;30;42m' + 'Video saved -> timelapse.mp4' + '\x1b[0m')
sys.exit()
