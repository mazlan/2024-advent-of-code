# Part 1
def check_valid_updates_and_sum():
    page_ordering_rules = []
    update_list = []
    line_break = False
    with open("input.txt") as f:
        for line in f:
            if line.strip() == "":
                line_break = True
                continue
            if line_break == False:
                ordering_rule = tuple(map(int, line.strip().split("|")))
                page_ordering_rules.append(ordering_rule)                
            else:
                update_to_check = tuple(map(int, line.strip().split(",")))
                update_list.append(update_to_check)
    sum_middle_index = 0
    for update in update_list:
        is_valid = True
        for i in range(len(update)-1):
            if (update[i], update[i+1]) not in page_ordering_rules:
                print("Invalid ordering: " + str(update))
                is_valid = False
                break
        if is_valid:
            middle_index = len(update) // 2
            sum_middle_index += update[middle_index]
    print(sum_middle_index)


# Part 2
def fix_invalid_updates_and_sum():
    page_ordering_rules = []
    update_list = []
    line_break = False
    with open("input.txt") as f:
        for line in f:
            if line.strip() == "":
                line_break = True
                continue
            if line_break == False:
                ordering_rule = tuple(map(int, line.strip().split("|")))
                page_ordering_rules.append(ordering_rule)                
            else:
                update_to_check = list(map(int, line.strip().split(",")))
                update_list.append(update_to_check)
    sum_middle_index = 0
    invalid_updates = []
    # Check first if update needs fixing and add to new list
    for update in update_list:
        for i in range(len(update)-1):
            if (update[i], update[i+1]) not in page_ordering_rules:
                invalid_updates.append(update)
                break

    # Fix invalid updates
    for invalid_update in invalid_updates:
        while True:
            needs_fixing = False
            for i in range(len(invalid_update)-1):
                if (invalid_update[i], invalid_update[i+1]) not in page_ordering_rules:
                    print("Invalid ordering: " + str(invalid_update) + ". Fixing...")
                    temp = invalid_update[i]
                    invalid_update[i] = invalid_update[i+1]
                    invalid_update[i+1] = temp
                    needs_fixing = True            
            if not needs_fixing:
                print("Final Fixed ordering: " + str(invalid_update))
                middle_index = len(invalid_update) // 2
                sum_middle_index += invalid_update[middle_index]
                break
    print(sum_middle_index)



if __name__ == "__main__":
    check_valid_updates_and_sum()
    fix_invalid_updates_and_sum()
