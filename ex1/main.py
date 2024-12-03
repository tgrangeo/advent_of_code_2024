
def part_one(first,second):
    distances = []
    for i in range(len(first)):
        distances.append(abs(int(first[i]) - int(second[i])))
    return sum(distances)


def part_two(first,second):
    similarity = []
    for i in range(len(first)):
        similarity.append(int(first[i]) * second.count(first[i]))
    return sum(similarity)
    

def main():
    with open("input.txt", "r") as f:
        raw_array = f.read().split()
    first = sorted(raw_array[::2])
    second = sorted(raw_array[1::2])
    print("differences =",part_one(first,second))
    print("similarity =",part_two(first,second))

if __name__ == "__main__":
    main()