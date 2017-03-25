#!/bin/zsh

#xinput --list-props "Wacom ISDv4 E6 Finger touch" | grep  -q 'Wacom Enable Touch (.*:.*1'
xinput --list-props "Wacom ISDv4 E6 Finger" | grep  -q 'Device Enabled (.*:.*1'
