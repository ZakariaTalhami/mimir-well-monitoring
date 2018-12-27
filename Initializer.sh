#!/bin/sh

# This file is placed in the /home/<user> with the script
# .profile, which should call this script.

# Prevent SSH logins from triggering this script
if [ -z "$SSH_CLIENT" ]
then
	# Kill any running python scripts
	ps aux | grep "[p]ython" | awk '{command=sprintf("kill %d", $2);system(command)}'
	echo "Running the code"
	
	# Initialize pigpiod
	sudo killall pigpiod
	sudo pigpiod
	
	# Make sure of working directory
	cd $(dirname $0)
	
	# Run Gateway scripts
	cd mimir-well-monitoring
	python reading_synch.py &
	python i2c_module.py &
	cd ..
	
	# Save running status
	ps aux | grep "[p]ython"  > runningGatewayScripts.txt

fi
