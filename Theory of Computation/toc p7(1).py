def is_equal_ones_zeroes(string):
    count = 0

    for char in string:
        if char == '1':
            count += 1
        elif char == '0':
            count -= 1
        else:
            return False
    
    return count == 0

test_cases = ["1100", "1010", "1001", "111000", "110011", "100101"]

for test in test_cases:
    result= is_equal_ones_zeroes(test)
    print(f"String: {test}, Accepted: {result}")