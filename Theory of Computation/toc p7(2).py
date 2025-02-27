def is_equal_ones_zeroes(string):
    count = 0

    for char in string:
        if char == 'a':
            count += 1
        elif char == 'b':
            count -= 1
        else:
            return False
    
    return count == 0

test_cases = ["aabb", "abab", "abba", "aaabbb", "aabbaa", "abbaba"]

for test in test_cases:
    result= is_equal_ones_zeroes(test)
    print(f"String: {test}, Accepted: {result}")