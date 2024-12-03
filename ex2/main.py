def is_safe(report):
	direction = 1 if report[0] > report[1] else 0
	for i in range(len(report) - 1):
		current = int(report[i])
		next_value =  int(report[i + 1])
		if direction == 1:  # Decreasing
			if current <= next_value or abs(current - next_value) >= 4:
				return False
		else:  # Increasing
			if current >= next_value or abs(current - next_value) >= 4:
				return False
	return True

def step_one(reports):
	safe = 0
	for report in reports:
		if len(report) < 2:
			continue
		if is_safe(report):
			safe += 1
	return safe

def step_two(reports):
	safe = 0
	for report in reports:
		if len(report) < 2:
			continue
		report = [int(x) for x in report]
		if is_safe(report):
			safe += 1
			continue
		is_safe_with_skip = False
		for i in range(len(report)):
			modified_report = report[:i] + report[i + 1:]
			if is_safe(modified_report):
				is_safe_with_skip = True
				break
		if is_safe_with_skip:
			safe += 1
	return safe


def main():
	with open("input.txt", "r") as f:
		raw_array = f.read().split('\n')
	reports = [line.split() for line in raw_array]
	print("part one :",step_one(reports))
	print("part two :",step_two(reports))
		
if __name__ == "__main__":
	main()