def is_divisible_by_4(number: float) -> bool:
    return number % 4 == 0

while True:
    try:
        num = float(input("Enter a decimal number: "))
        if is_divisible_by_4(num):
            print(f"{num} is divisible by 4.")
            break
        else:
            print(f"{num} is not divisible by 4. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
