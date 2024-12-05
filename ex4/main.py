def check_horizontal(raw_data, to_find):
	array = raw_data.split()
	count = 0
	word_len = len(to_find)
	for row in array:
		for i in range(len(row) - word_len + 1):
			if row[i:i + word_len] == to_find:
				count += 1
	return count

def check_vertical(raw_data, to_find):
	array = raw_data.split()
	count = 0
	num_rows = len(array)
	num_cols = len(array[0]) if num_rows > 0 else 0
	word_len = len(to_find)
	for col in range(num_cols):
		for row in range(num_rows - word_len + 1):
			if all(array[row + i][col] == to_find[i] for i in range(word_len)):
				count += 1
	return count

def check_diagonal(raw_data, to_find):
	array = raw_data.split()
	count = 0
	num_rows = len(array)
	num_cols = len(array[0]) if num_rows > 0 else 0
	word_len = len(to_find)

	for row in range(num_rows - word_len + 1):
		for col in range(num_cols - word_len + 1):
			if all(array[row + i][col + i] == to_find[i] for i in range(word_len)):
				count += 1

	for row in range(num_rows - word_len + 1):
		for col in range(word_len - 1, num_cols):
			if all(array[row + i][col - i] == to_find[i] for i in range(word_len)):
				count += 1

	for row in range(word_len - 1, num_rows):
		for col in range(num_cols - word_len + 1):
			if all(array[row - i][col + i] == to_find[i] for i in range(word_len)):
				count += 1

	for row in range(word_len - 1, num_rows):
		for col in range(word_len - 1, num_cols):
			if all(array[row - i][col - i] == to_find[i] for i in range(word_len)):
				count += 1

	return count

def find_X_MAS(raw_data):
    grid = [list(row) for row in raw_data.split()]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == "A":
                if  grid[row - 1][col - 1] == "M" and grid[row - 1][col + 1] == "M" and grid[row + 1][col - 1] == "S" and grid[row + 1][col + 1] == "S":
                    count += 1
                if grid[row - 1][col - 1] == "S" and grid[row - 1][col + 1] == "M" and grid[row + 1][col - 1] == "S" and grid[row + 1][col + 1] == "M":
                    count += 1
                if grid[row - 1][col - 1] == "M" and grid[row - 1][col + 1] == "S" and grid[row + 1][col - 1] == "M" and grid[row + 1][col + 1] == "S":
                    count += 1
                if  grid[row - 1][col - 1] == "S" and grid[row - 1][col + 1] == "S" and grid[row + 1][col - 1] == "M" and grid[row + 1][col + 1] == "M":
                    count += 1
    return count

def main():
	with open("input.txt", "r") as f:
		raw_data = f.read()
		
	count = 0
	count += check_horizontal(raw_data, "XMAS")
	count += check_vertical(raw_data, "XMAS")
	count += check_diagonal(raw_data, "XMAS")
	count += check_horizontal(raw_data, "SAMX")
	count += check_vertical(raw_data, "SAMX")
	print("Part_One", count)
 
 
	print("Part_two", find_X_MAS(raw_data))

if __name__ == "__main__":
	main()
