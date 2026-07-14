"""
Project: Smart Calculator
Author: Joshitha sree
Version: 1.0
Description:
A command-line calculator built using Python.
This project is part of my GitHub Engineering Portfolio.
"""

def main_menu():
    print("=" * 50)
    print("      scientific calculator")
    print("=" * 50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. exit")

def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The result of addition is: {result}")

def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The result of subtraction is: {result}")

def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The result of multiplication is: {result}")

def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of division is: {result}")
def menu():
    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")      

if __name__ == "__main__":
    menu()           