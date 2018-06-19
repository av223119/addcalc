def add(numbers):
    if numbers == "":
        return 0
    lst = numbers.split(",", 1)
    return sum(map(lambda x: int(x), lst))
