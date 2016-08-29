FROM frolvlad/alpine-python3:latest
WORKDIR health_check
ENV humidity_data=humidity.csv
ENV temperature_data=temperature.csv
COPY health_check.py disease_checker.py diseases.py $humidity_data $temperature_data ./
ENTRYPOINT ./health_check.py $humidity_data $temperature_data
