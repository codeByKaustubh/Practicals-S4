#Program 1:  Design a python program for creating a machine which count number of 1’s and 0’s in a given string.  
def count_ones_zeroes(binary_string):
    ones_count = binary_string.count('1')
    zeroes_count = binary_string.count('0')
    return ones_count, zeroes_count

if __name__ == "__main__":
    binary_string = input("Enter a binary string: ")
    ones, zeroes = count_ones_zeroes(binary_string)
    print(f"Number of 1's: {ones}")
    print(f"Number of 0's: {zeroes}")
