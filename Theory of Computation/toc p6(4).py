def is_divisible_by_5(number: float) -> bool:
    return number % 5 == 0

while True:
    try:
        num = float(input("Enter a decimal number: "))
        if is_divisible_by_5(num):
            print(f"{num} is divisible by 5.")
            break
        else:
            print(f"{num} is not divisible by 5. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
