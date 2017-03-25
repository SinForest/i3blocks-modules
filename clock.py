#!/usr/bin/python2
# coding=UTF-8

import sys
import os

#import subprocess

import re
import commands

import time

day_color = {
	"0" : "red",
	"1" : "cyan",
	"2" : "yellow",
	"3" : "DeepPink",
	"4" : "lime",
	"5" : "Orange",
	"6" : "blue"
}

s_zth = "<span face='monospace' color='" + day_color[time.strftime("%w")] +"'>" + time.strftime("%a") + "</span>"
s_fst = "<span face='monospace'>" + time.strftime(" %Y-%m-") + "</span>"
s_snd = "<b><span face='monospace'>" + time.strftime("%d") + "</span></b>"
if time.strftime("%H:%M") == "04:20" or time.strftime("%H:%M") == "16:20" or os.path.isfile("/tmp/420mode"):
	s_trd = "<span face='monospace' color='Chartreuse'> 4:20 </span><span face='monospace'>" + time.strftime("%S") + "</span>"
else:
	s_trd = "<span face='monospace'>" + time.strftime(" %H:%M:%S") + "</span>"

print(s_zth + s_fst + s_snd + s_trd)


"""
print("<span font_desc='FontAwesome' color='" + s_color + "'>" + s_state.encode('ascii', 'xmlcharrefreplace') +\
	"</span><span face='monospace' color='white'>"  + s_percent + "</span><span color='" + s_color + "'> [" + s_time + "]" + "</span>")
"""
#color='" + s_color + "'
