"""
give two numbers and operation to calculate result
like 1+1 = 2
"""
if __name__ == '__main__':
    try:
        number1 = float(input("please input operation Number1: "))
        number2 = float(input("please input operation Number2: "))
    except ValueError:
        print("Please input a valid number.")
        exit()  # like sys.exit(1)

    operation = input("please input operation,support + - * / or // ")
    if operation == "+":
        print(f"{number1} {operation} {number2} = {number1 + number2}")
    elif operation == "-":
        print(f"{number1} {operation} {number2} = {number1 - number2}")
    elif operation == "*":
        print(f"{number1} {operation} {number2} = {number1 * number2}")
    elif operation == "/":
        if number2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"{number1} {operation} {number2} = {number1 / number2}")
    elif operation == "//":
        if number2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"{number1} {operation} {number2} = {number1 / number2}")
    else:
        print("Unsupported operation.")
