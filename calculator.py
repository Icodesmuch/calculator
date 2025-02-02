def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b


def calculator():
    print("Welcome to the calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice: ")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        exit()

    try:
        if choice == "1":
            print(addition(a, b))
        elif choice == "2":
            print(subtraction(a, b))
        elif choice == "3":
            print(multiplication(a, b))
        elif choice == "4":
            print(division(a, b))
        else:
            print("Invalid choice")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")



if __name__=="__main__":
    calculator()