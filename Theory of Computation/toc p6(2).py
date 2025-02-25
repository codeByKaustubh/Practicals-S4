def is_divisible_by_3(number: float) -> bool:
    return number % 3 == 0

while True:
    try:
        num = float(input("Enter a decimal number: "))
        if is_divisible_by_3(num):
            print(f"{num} is divisible by 3.")
            break
        else:
            print(f"{num} is not divisible by 3. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")
