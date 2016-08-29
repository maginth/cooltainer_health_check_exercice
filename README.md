This is a simple health check exercise in python.

usage :
> ./health_chech.py <humidity.csv> <temperature.csv>

Or use docker by running the following commands :
> $ docker build -t health_check .  
> $ docker run health_check | tee -a health.log
