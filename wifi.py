#!/usr/bin/python2
# coding=UTF-8

import sys
import re
import commands
import os

#s_percent = commands.getstatusoutput("/usr/lib/i3blocks/wifi")[1].split('\n')[0]
s_percent  = commands.getstatusoutput("grep wlp3s0 /proc/net/wireless | awk '{ print int($3 * 100 / 70) }'")[1]

if s_percent == "":
	s_ssid = "X"
	s_color = "#bb000"
else:
	i_percent = int(s_percent)
	s_percent = "(" + s_percent.rjust(3) + "%)"
	#s_ssid = commands.getstatusoutput("/sbin/iwconfig 2>&1 | grep wlan | grep -o 'ESSID:\".*\"'")[1][7:-1]
	s_ssid = commands.getstatusoutput("iw dev wlp3s0 link | grep SSID")[1]
	match = re.search("\s+SSID: (.*)", s_ssid)
	s_ssid = match.group(1)

	c_red = [255, 0, 0]
	c_yellow = [255, 210, 0]
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

#
#s_status = ""

#420
if os.path.isfile("/tmp/420mode"):
	s_color = "Chartreuse"
	s_percent = "(420)"
#420!

print("<span font_desc='FontAwesome' color='" + s_color + "'>" + u": </span><span color='cyan'>".encode('ascii', 'xmlcharrefreplace')\
	+ s_ssid + " </span><span face='monospace' color='" + s_color + "'>" + s_percent + "</span>")
