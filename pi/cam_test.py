#!/usr/bin/python

#Camera test program

import picamera

from time import sleep

camera = picamera.PiCamera()

camera.capture('../../../image.jpg')

camera.start_preview()
sleep(10.0)
camera.stop_preview()
