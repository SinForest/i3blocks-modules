#!/usr/bin/python2
# coding=UTF-8

import sys

#import subprocess

import re
import commands

i_percent = int(float(commands.getstatusoutput("xbacklight")[1]))

c_white = [255, 255, 255]
c_grey = [100, 140, 140]

if i_percent > 100:
	i_percent = 100
if i_percent < 0:
	i_percent = 0

color = [0,0,0]
p = i_percent * 0.01
for i in range(0,3):
	color[i] =  int(c_white[i] * p + c_grey[i] * (1-p))
s_color = "#" + str(hex(color[0]))[2:].zfill(2) + str(hex(color[1]))[2:].zfill(2) + str(hex(color[2]))[2:].zfill(2)

print("<span font_desc='FontAwesome' color='" + s_color + "'>" + str(i_percent) + "%</span>")
