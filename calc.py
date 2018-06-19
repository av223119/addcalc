import re

def add(numbers):
    if numbers == "":
        return 0
    lst = re.split(r"[,\n]", numbers)
    return sum(map(lambda x: int(x), lst))
