import re

def part_one(raw_input):
	muls = re.findall("mul\(\d+,\d+\)",raw_input)
	res = 0
	for m in muls:
		t = re.findall(r'\d+', m)
		res = res + int(t[0]) * int(t[1])
	return res
 
def part_two(raw_input):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    tokens = re.findall(pattern, "".join(raw_input))
    enabled = True
    res = 0
    for t in tokens:
        if t[0] == "do()":
            enabled = True
        elif t[0] == "don't()":
            enabled = False
        elif enabled and t[0].startswith("mul("):
            res = res + int(t[1]) * int(t[2])
    return res

def main():
	with open("input.txt", "r") as f:
		raw_input = f.read()
	print(part_one(raw_input))
	print(part_two(raw_input))
		
if __name__ == "__main__":
	main()