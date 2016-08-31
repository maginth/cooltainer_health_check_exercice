This is a simple health check exercise in python.

The diseases.py file is designed to be easily edited by anyone.
The script output log warnings whenever a threat defined in diseases.py is detected.

usage :
> ./health_check.py \<humidity.csv\> \<temperature.csv\>

Or use docker by running the following commands :
> $ docker build -t health_check .  
> $ docker run health_check | tee -a health.log
