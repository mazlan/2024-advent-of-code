def distance_between_groups():
    groupA = []
    groupB = []
    total_distance = 0

    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        groupA.append(int(line.split()[0]))
        groupB.append(int(line.split()[1]))
    sorted_groupA = sorted(groupA)
    sorted_groupB = sorted(groupB)
    for val1, val2 in zip(sorted_groupA, sorted_groupB):
        distance = abs(val1 - val2)
        total_distance += distance
    print(total_distance)
    return total_distance


if __name__ == "__main__":
    distance_between_groups()    