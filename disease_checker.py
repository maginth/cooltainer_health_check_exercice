import sys

check_list = [];
active_diseases = set()

def exposition_time(condition_duration):
	def disease_condition(condition):
		t0  = sys.maxsize
		def checker(time, hum, temp):
			nonlocal t0
			if not condition(hum, temp):
				t0 = time
				return ''
			elif time - t0 >= condition_duration:
				active_diseases.add(condition.__name__)
				t0 = time
				return condition.__name__ + " detected"

		check_list.append(checker)
		return checker
	return disease_condition
