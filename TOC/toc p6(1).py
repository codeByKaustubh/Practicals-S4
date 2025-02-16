def is_divisible_by_2(number: float) -> bool:
    return number % 2 == 0

while True:
    try:
        num = float(input("Enter a decimal number: "))
        if is_divisible_by_2(num):
            print(f"{num} is divisible by 2.")
            break
        else:
            print(f"{num} is not divisible by 2. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
