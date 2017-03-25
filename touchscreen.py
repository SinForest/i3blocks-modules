#!/usr/bin/python
# coding=UTF-8

import subprocess
import os

dir = os.path.dirname(__file__)
filename_touch = os.path.join(dir, './check_touch.sh')
filename_pad = os.path.join(dir, './check_pad.sh')

touch = subprocess.call([filename_touch])
pad = subprocess.call([filename_pad])

s1 = "<span font_desc='FontAwesome' color='" + ("#FF1177" if pad == 1 else "#11FF77") + "'></span>"
s2 = "<span font_desc='FontAwesome' color='" + ("#FF1177" if touch == 1 else "#11FF77") + "'></span>"

sep = "<span color='" + ("#FF1177" if touch + pad == 2 else "#11FF77" if touch + pad == 0 else "#EEEE77") + "'> - </span>"

print(s2 + sep + s1)
