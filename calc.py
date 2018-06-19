import re

def add(numbers):
    del_spec = re.fullmatch(r"//\[(.)\]\n(.*)", numbers)
    sep = r"[,\n]"
    if del_spec:
        numbers = del_spec.group(2)
        sep = del_spec.group(1)
    if numbers == "":
        return 0
    lst = re.split(sep, numbers)
    return sum(map(lambda x: int(x), lst))
