for number in range(10):
    for digits in range(number + 1, 10):
        print("{:d}{:d}" .format(number, digits), end=", " if digits != 9 or number != 8 else "\n")
        