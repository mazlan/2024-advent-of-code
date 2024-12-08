import re

# Part 1
def sum_uncorrupted_mul():
    mul_list = []
    # implement regex to extract out all mul(x,y)
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    mul_list = [match for line in open("input.txt") for match in mul_pattern.findall(line)]
    total = sum(int(x) * int(y) for x, y in mul_list)
    print(total)
    return total

# Part 2
def sanitize_input(input_str):
    # Initialize flag
    start_deleting = False
    sanitized_input = []
    
    # Process character by character
    i = 0
    while i < len(input_str):
        # Check for control sequences
        if input_str[i:i+7] == "don't()":
            start_deleting = True
            i += 7
            continue
        elif input_str[i:i+4] == "do()":
            start_deleting = False
            i += 4
            continue            
        #If not deleting then append to sanitized_input
        if not start_deleting:
            sanitized_input.append(input_str[i])
        i += 1        
    return ''.join(sanitized_input)

def sum_mul_clean():
    # Read input
    s = open("input.txt").read()
    
    # Sanitize the input
    sanitized_input = sanitize_input(s)
    
    # Find and sum multiplications
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = pattern.findall(sanitized_input)
    total = sum(int(x) * int(y) for x, y in matches)
    print(total)
    return total



if __name__ == "__main__":
    sum_uncorrupted_mul()
    sum_mul_clean()
