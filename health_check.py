#! /usr/bin/python3

import sys
from diseases import check_list
from datetime import datetime

if len(sys.argv) != 3:
	print("usage : " + sys.argv[0] + " <humidity_data.cvs> <temperature_data.cvs>",file=sys.stderr)
	exit(-1)

humidity, temperature = open(sys.argv[1]), open(sys.argv[2])
# skip the column names
humidity.readline()
temperature.readline()

#apply the check list
for line in humidity:
	date, hum_str  = line.strip().split(",")

	time = datetime.strptime(date, "%d/%m/%Y %H:%M:%S").timestamp() / 60
	hum = float(hum_str)
	temp = float(temperature.readline().strip().split(",")[1])
	for check in check_list:
		res = check(time, hum, temp)
		if res:
			print(date, res)