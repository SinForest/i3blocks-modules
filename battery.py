#!/usr/bin/python2
# coding=UTF-8

import sys
import os

#import subprocess

import re
import commands

s_percent = commands.getstatusoutput("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep percentage | grep -o '[0-9]*%'")[1]
i_percent = int(s_percent[:-1])
s_percent = s_percent.rjust(4)

s_state = commands.getstatusoutput("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep state | grep -o ':\s*\w*' | grep -o '\w*'")[1]

s_time_raw = commands.getstatusoutput("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep 'time to ' | grep -o '[0-9]*,[0-9]*\s\w*'")[1]

m = re.search("\d+,\d+", s_time_raw)
if(m):
	s_time_value = m.group(0)
try:
    s_time_value
except NameError:
    s_time_value = ""

m = re.search("[a-z]+", s_time_raw)
if(m):
	s_time_unit = m.group(0)
try:
    s_time_unit
except NameError:
    s_time_unit = ""

if s_state == "charging":
	if i_percent > 90:
		s_state = u" "
	elif i_percent > 65:
		s_state = u" "
	elif i_percent > 40:
		s_state = u" "
	elif i_percent > 15:
		s_state = u" "
	else:
		s_state = u" "
elif s_state == "fully":
	s_state = u""
elif s_state == "discharging":
	if i_percent > 90:
		s_state = u""
	elif i_percent > 65:
		s_state = u""
	elif i_percent > 40:
		s_state = u""
	elif i_percent > 15:
		s_state = u""
	else:
		s_state = u""

c_red = [255, 0, 0]
c_yellow = [255, 255, 0]
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


s_time = "00:00"
if s_time_unit == "minutes":
	s_time = "00:" + re.search("[0-9]+", s_time_value).group(0).zfill(2)
elif s_time_unit == "hours":
	s_time = re.search("^\d+", s_time_value).group(0) + ":" + str(int(float("0." + re.search("\d+$", s_time_value).group(0)) * 60)).zfill(2)

#420
if os.path.isfile("/tmp/420mode"):
	s_color = "Chartreuse"
	s_time = "4:20"
#420!

print("<span font_desc='FontAwesome' color='" + s_color + "'>" + s_state.encode('ascii', 'xmlcharrefreplace') +\
	"</span><span face='monospace' color='white'>"  + s_percent + "</span><span color='" + s_color + "'> [" + s_time + "]" + "</span>")
#color='" + s_color + "'
