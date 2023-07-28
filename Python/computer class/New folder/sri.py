import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiate(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

print("Scientific Calculator")

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Sine")
    print("7. Cosine")
    print("8. Tangent")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        print("Exiting the calculator...")
        break

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            if num2 != 0:
                print("Result:", divide(num1, num2))
            else:
                print("Error: Cannot divide by zero!")
        elif choice == '5':
            print("Result:", exponentiate(num1, num2))
    elif choice in ['6', '7', '8']:
        angle = float(input("Enter the angle in degrees: "))

        if choice == '6':
            print("Result:", sine(angle))
        elif choice == '7':
            print("Result:", cosine(angle))
        elif choice == '8':
            print("Result:", tangent(angle))
    else:
        print("Invalid choice. Please select a valid operation.")
