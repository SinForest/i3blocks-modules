#!/usr/bin/python3

import os.path

if os.path.isfile("/tmp/420mode"):
	os.remove("/tmp/420mode")
else:
	open("/tmp/420mode", 'a').close()
