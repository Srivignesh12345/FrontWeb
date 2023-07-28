def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_cubes = 0
    for digit in num_str:
        sum_of_cubes += int(digit) ** num_digits
    return sum_of_cubes == number
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")