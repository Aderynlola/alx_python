def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    list = [0, 1]
    while len(list) < n:
        nextnumber = list[-1] + list[-2]
        list.append(nextnumber)

    return list
