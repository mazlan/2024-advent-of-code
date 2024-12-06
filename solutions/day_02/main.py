# Sample Input Example
# 75 78 81 82 80
# 14 15 18 21 24 26 28 28
# 61 63 64 66 68 70 73 77
# 13 14 17 18 19 26
# 60 63 65 62 63 66 69 70
# 18 21 23 25 28 26 29 26


# This works for puzzle 1 but i need a separate function for is_valid_sequence for puzzle 2
def find_safe_report_count():
    safe_report_count = 0    
    with open("input.txt") as file:
        for line in file:
            valid_ascending_count = 0
            valid_descending_count = 0
            report = list(map(int, line.split()))        
            # Check if the numbers are in ascending order or descending order
            for i in range(1, len(report)):
                if (report[i] > report[i - 1]) and (report[i] - report[i - 1] <= 3):
                    valid_ascending_count += 1
                elif (report[i] < report[i - 1]) and (report[i - 1] - report[i] <= 3):
                    valid_descending_count += 1                    
                else:
                    # if the numbers are equal or the difference is greater than 3, discard the report as unsafe
                    break
            if valid_ascending_count == (len(report) - 1) or valid_descending_count == (len(report) - 1):
                safe_report_count += 1
    print(safe_report_count)    
    return safe_report_count


def is_valid_sequence(report):
    ascending = descending = True
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <=abs(diff) <= 3):
            ascending = descending = False
            break
        if diff > 0:
            descending = False
        elif diff < 0:
            ascending = False    
    return ascending or descending


def find_safe_report_count_with_tolerance():
    safe_report_count = 0
    with open("input.txt") as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_valid_sequence(report):
                safe_report_count += 1
                continue
            for i in range(len(report)):
                removed_level = report.pop(i)
                if is_valid_sequence(report):
                    safe_report_count += 1
                    report.insert(i, removed_level)
                    break
                report.insert(i, removed_level)        
        print(safe_report_count)
        return safe_report_count


if __name__ == "__main__":
    find_safe_report_count()
    find_safe_report_count_with_tolerance()