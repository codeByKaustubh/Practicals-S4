def count_as_bs(input_string):
    a_count = input_string.count('a')
    b_count = input_string.count('b')
    
    return a_count, b_count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    a_count, b_count = count_as_bs(input_string)
    print(f"Number of a's: {a_count}")
    print(f"Number of b's: {b_count}")