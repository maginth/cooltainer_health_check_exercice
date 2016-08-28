from disease_checker import *

@exposition_time(90)
def oidium_sporulation(hum, temp):
	return hum > 90

@exposition_time(360)
def botrytis(hum, temp):
	return hum > 90 and 15 < temp < 20

@exposition_time(600)
def oidium_development_risk(hum, temp):
	return "oidium_sporulation" in active_diseases and hum < 70 and temp > 20

