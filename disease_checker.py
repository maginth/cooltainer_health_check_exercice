import sys

check_list = [];
active_diseases = set()

def exposition_time(condition_duration):
	def disease_condition(condition):
		total_exposition_time  = 0
		last_check_time = 0
		last_condition = False
		def checker(time, hum, temp):
			nonlocal total_exposition_time
			nonlocal last_check_time
			nonlocal last_condition
			
			current_condition = condition(hum, temp)

			if (current_condition or last_condition) and last_check_time:
				total_exposition_time += time - last_check_time;

			last_check_time = time
			last_condition = current_condition

			if total_exposition_time > condition_duration:
				active_diseases.add(condition.__name__)
				total_exposition_time  = 0
				return condition.__name__ + " detected"
			else:
				return ''

		check_list.append(checker)
		return checker
	return disease_condition
