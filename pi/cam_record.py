#!/usr/bin/python

#Camera test program

import picamera

from time import sleep

camera = picamera.PiCamera()

camera.capture('../../../image.jpg')

camera.start_recording('../../../video.h264')
sleep(10.0)
camera.stop_recording()
