#!/usr/bin/python2
# coding=UTF-8

import sys
import os

#import subprocess

import re
import commands

disk = commands.getstatusoutput('lsblk | grep " /$"')[1].split('\n')[0]
match = re.search("sd\w\d", disk)
if match:
	disk = match.group(0)
else:
	disk = "sda1"

res = commands.getstatusoutput("df -h | grep /dev/{}".format(disk))[1]
rx = "\/dev\/sdb3\s+\d+\w\s+\d+,?\d*\w+\s+(\d+\w)\s+(\d+)%"
match = re.search(rx, res)

if match:
	s_free = match.group(1)
	i_percent = int(match.group(2))
	if i_percent > 100:
		i_percent = 100
	if i_percent < 0:
		i_percent = 0
else:
	s_free = "---"
	i_percent = 0

i_percent = 100 - i_percent #mieser hack v2

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
	s_free = "420G"
#420!

print("<span font_desc='FontAwesome' color='" + s_color + u"'>: </span><span face='monospace'>".encode('ascii', 'xmlcharrefreplace')\
	+ s_free + "</span>")
