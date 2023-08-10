"""Write a program that asks the user to enter a series of numbers separated by , and returns the average, maximum,
and minimum of those numbers. """
if __name__ == '__main__':
    user_input = input("Please enter a list of numbers separated by commas: ")
    try:
        number_list = [float(item.strip()) for item in user_input.split(",")]
    except ValueError:
        print("input should be a number")
        exit()
    total = 0.0
    maximum = 0.0
    minimum = 0.0
    for index, num in enumerate(number_list):
        if index == 0:
            maximum = num
            minimum = num
        else:
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num
        total += num
    print(f"maximum number is {maximum}, minimum number is {minimum}, average is {total / len(number_list)}")
    # way 2 test
    maximum = max(number_list)
    minimum = min(number_list)
    average = sum(number_list) / len(number_list)
    print(f"maximum number is {maximum}, minimum number is {minimum}, average is {total / len(number_list)}")
