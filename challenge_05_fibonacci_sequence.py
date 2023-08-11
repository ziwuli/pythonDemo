"""
Create a function that calculates the nth term of the Fibonacci sequence
"""


def get_fibonacci_sequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    first, second = 0, 1
    while n > 2:
        c = first + second
        first = second
        second = c
        n -= 1
    else:
        return c


if __name__ == '__main__':
    try:
        user_input = int(input("please input a sequence number: "))
    except ValueError:
        print("Please input a valid number.")
        exit()
    if user_input <= 0:
        print("Please input a valid number. should be greater than 0")
    else:
        print(f"Fibonacci sequence {user_input} is {get_fibonacci_sequence(user_input)}")

