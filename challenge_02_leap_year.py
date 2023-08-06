"""
Write a program to determine whether a year is a leap year
return can't used into module code, can use exit()
"""
if __name__ == '__main__':
    try:
        year = int(input("please input a year: "))
    except ValueError:
        print("Year verification failed")
        exit()
    if year <= 0:
        print("Year verification failed")
        exit()
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
