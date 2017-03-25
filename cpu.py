#!/usr/bin/python2
# coding=UTF-8

import sys
import re
import commands
import os

s_percent = commands.getstatusoutput("/usr/lib/i3blocks/cpu_usage")[1].split('\n')[0]
f_percent = float(s_percent[:-1])
s_percent = s_percent.rjust(7)
#Mieser Woraround, weil zu faul
i_percent = 100 - int(f_percent)

c_red = [255, 0, 0]
c_yellow = [255, 166, 0]
c_green = [0, 255, 0]

if i_percent > 100:
	i_percent = 100
if i_percent < 0:
	i_percent = 0

color = [0,0,0]
if i_percent > 50:
	p = (i_percent - 50) * 0.02
else:
	p = i_percent * 0.02
for i in range(0,3):
	color[i] =  int(c_green[i] * p + c_yellow[i] * (1-p) if i_percent > 50 else c_yellow[i] * p + c_red[i] * (1- p))
s_color = "#" + str(hex(color[0]))[2:].zfill(2) + str(hex(color[1]))[2:].zfill(2) + str(hex(color[2]))[2:].zfill(2)

#420
if os.path.isfile("/tmp/420mode"):
	s_color = "Chartreuse"
	s_percent = "  4.20%"
#420!

print("<span font_desc='FontAwesome' color='" + s_color + u"'>:</span><span face='monospace'>".encode('ascii', 'xmlcharrefreplace')\
	+ s_percent + "</span>")
