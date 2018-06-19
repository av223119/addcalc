def add(numbers):
    if numbers == "":
        return 0
    lst = numbers.split(",")
    return sum(map(lambda x: int(x), lst))
