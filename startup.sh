#!/bin/bash

# Startup script to run record.py 


# Activate the venv: 
source /home/bugs/.venv/bin/activate > /home/bugs/Desktop/AutoBeetle-BeetleMonitoring/logfile.log 2>&1 &


# Move to the project github
cd /home/bugs/Desktop/AutoBeetle-BeetleMonitoring/ > /home/bugs/Desktop/AutoBeetle-BeetleMonitoring/logfile.log 2>&1 &


# Run your record.py and append outputs to log file 
python3 record.py  >> logfile.log 2>&1 &


# Display the contents of the log file in a terminal window
x-terminal-emulator -e "tail -f logfile.log"