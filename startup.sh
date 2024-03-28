#!/bin/bash

# Startup script to run record.py 

# Activate the venv and move to the project directory
source /home/bugs/.venv/bin/activate && cd /home/bugs/Desktop/AutoBeetle-BeetleMonitoring/ 

# Run your record.py and append outputs to log file 
python3 record.py >> /home/bugs/Desktop/AutoBeetle-BeetleMonitoring/logfile.log 2>&1 &

# Display the contents of the log file in a terminal window
x-terminal-emulator -e "tail -f /home/bugs/Desktop/AutoBeetle-BeetleMonitoring/logfile.log"
