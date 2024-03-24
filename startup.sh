#!/bin/bash

# Startup script to run record.py 


# Activate the venv: 
source .venv/bin/activate > /Desktop/AutoBeetle-BeetleMonitoring/logfile.log 2>&1


# Move to the project github
cd /Desktop/AutoBeetle-BeetleMonitoring/


# Run your record.py and append outputs to log file 
python3 record.py  >> logfile.log 2>&1


# Print the last line of the log file: 

tail -f logfile.log