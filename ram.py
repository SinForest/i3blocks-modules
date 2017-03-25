#!/usr/bin/python2
# coding=UTF-8

import sys
import os

#import subprocess

import re
import commands

inputFile = open("/proc/meminfo", "r")
res = inputFile.read()

rx = "MemTotal:\s+(\d+)\s+kB[\s\S]*MemAvailable:\s+(\d+)\s+kB"
match = re.search(rx, res)
threshold = 300000

if match:
	i_total = int(match.group(1)) - threshold #bc something's always used ;)
	i_free = float(match.group(2))
	i_percent = i_free * 100 / i_total
	s_unit = "k"
	if i_percent > 100:
		i_percent = 100
	if i_percent < 0:
		i_percent = 0
	if i_free > 1024:
		i_free /= 1024
		s_unit = "M"
	if i_free > 1024:
		i_free /= 1024
		s_unit = "G"
	if i_free > 1024:
		i_free /= 1024
		s_unit = "T"
	s_free = str(i_free)[0:3]


else:
	s_free = "---"
	i_percent = 0

#i_percent = 100 - i_percent #mieser hack v2

#!!
#i_percent = 20

c_red = [255, 0, 0]
c_yellow = [255, 166, 0]
c_green = [0, 255, 0]

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
	s_free = "420"
	s_unit = "g"
#420!

print("<span font_desc='FontAwesome' color='" + s_color + u"'>: </span><span face='monospace'>".encode('ascii', 'xmlcharrefreplace')\
	+ s_free + s_unit + "</span>")
