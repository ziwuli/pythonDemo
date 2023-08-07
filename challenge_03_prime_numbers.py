"""
Write a program to find all prime numbers in a given range
"""
import math


def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt = int(math.sqrt(number))
    for n in range(3, sqrt + 1, 2):  # 从3开始，步长为2，这样只会检查奇数
        if number % n == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        start = int(input("please input a start number: "))
        end = int(input("please input a end number: "))
    except ValueError:
        print("input should be a number")
        exit()
    if start <= 1 or end <= 1 or start > end:
        print("start or end less or equal than 1 and end should greater or equal to start.")
        exit()
    result_way1 = [i for i in range(start, end+1) if is_prime(i)]
    result_way2 = []
    for i in range(start, end+1):
        isPrime = is_prime(i)
        if isPrime:
            result_way2.append(i)
    print(result_way1)
    print(result_way2)

