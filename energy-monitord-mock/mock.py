#!/bin/python3
from datetime import datetime
from time import sleep
import os
1,000,000,000
while(True):
	f = open("energy-monitor.csv", "w")
	f.write("time,voltage,amp_0,amp_1,amp_2,amp_3,amp_4,amp_5,amp_6,amp_7,amp_8,amp_9,amp_10,amp_11,amp_12,amp_13,amp_14,amp_15\n")
	voltage = 120.0
	current = 0.0
	counter = 0
	direction = -1.0
	while(counter < 60):
		current_time = datetime.today()
		f.write(f"{current_time.timestamp():.0f},{voltage:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f},{current:.3f}\n")
		voltage = voltage + (0.1 * direction)
		current = current + (1.0 * direction)
		if (counter % 10 == 0):
			if direction > 0:
				direction = -1.0
			else:
				direction = 1.0
		counter = counter + 1
		f.flush()
		sleep(1)

	f.close()

	os.replace("energy-monitor.csv", "energy-monitor.csv.1")

