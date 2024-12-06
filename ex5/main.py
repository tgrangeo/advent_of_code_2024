def first_part(raw_data):
	data = raw_data.split("\n\n")[0]
	rules = [tuple(int(num) for num in r.split('|')) for r in data.split("\n")]
	to_check = raw_data.split("\n\n")[1].split('\n')
	to_check = [r.split(',') for r in to_check]
	to_check = [[int(num) for num in r if num.strip()] for r in to_check]
	res = to_check.copy()
	for r in to_check:
		for x, y in rules:
			if x in r and y in r:
				x_index = r.index(x)
				y_index = r.index(y)
				if y_index < x_index:
					if r in res:
						res.remove(r)
	middle = 0
	for r in res:
		if len(r) > 0:
			middle += r[len(r)//2]
	return middle

def second_part(raw_data):
	data = raw_data.split("\n\n")[0]
	rules = [tuple(int(num) for num in r.split('|')) for r in data.split("\n")]
	to_check = raw_data.split("\n\n")[1].split('\n')
	to_check = [r.split(',') for r in to_check]
	to_check = [[int(num) for num in r if num.strip()] for r in to_check]
	res = []
	for r in to_check:
		modified = True
		to_add = False
		while modified: 
			modified = False
			for x, y in rules:
				if x in r and y in r:
					x_index = r.index(x)
					y_index = r.index(y)
					if y_index < x_index:
						r[x_index], r[y_index] = r[y_index], r[x_index]
						modified = True
						to_add = True
		if to_add:
			res.append(r)
	return sum(r[len(r) // 2] for r in res if r)

def main():
	with open("input.txt") as f:
		raw_data = f.read()
	first = first_part(raw_data)
	print("first:" , first)
	second = second_part(raw_data)
	print("second:", second)
 

if __name__ == "__main__":
	main()
