#Program 1:  Design a python program for creating a machine which count number of 1’s and 0’s in a given string.  
def count(binary_string):
    onec = binary_string.count('1')
    zeroc = binary_string.count('0')
    return onect, zeroc

if __name__ == "__main__":
    binary_string = input("Enter a binary string: ")
    one, zero = count(binary_string)
    print(f"Number of 1's: {one}")
    print(f"Number of 0's: {zero}")
