from collections import Counter

def get_sorted_groups():
    groupA = []
    groupB = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        groupA.append(int(line.split()[0]))
        groupB.append(int(line.split()[1]))
    sorted_groupA = sorted(groupA)
    sorted_groupB = sorted(groupB)
    return sorted_groupA, sorted_groupB

def distance_between_groups():
    sorted_groupA, sorted_groupB = get_sorted_groups()
    total_distance = 0
    for val1, val2 in zip(sorted_groupA, sorted_groupB):
        distance = abs(val1 - val2)
        total_distance += distance
    print(total_distance)
    return total_distance

def calculate_similarity_score():
    sorted_groupA, sorted_groupB = get_sorted_groups()
    total_similarity_score = 0
    for val1 in sorted_groupA:
        total_count = 0
        for val2 in sorted_groupB:
            if val1 == val2:
                total_count += 1
        similarity_score =  val1 * total_count
        total_similarity_score += similarity_score
    print(total_similarity_score)
    return total_similarity_score

def calculate_similarity_score_improved_O_n_version():
    sorted_groupA, sorted_groupB = get_sorted_groups()
    count_groupB = Counter(sorted_groupB)
    total_similarity_score = sum(
        val * count_groupB[val] 
        for val in sorted_groupA
        if val in count_groupB
    )
    print(total_similarity_score)
    return total_similarity_score
    

if __name__ == "__main__":
    distance_between_groups()
    calculate_similarity_score()
    calculate_similarity_score_improved_O_n_version()