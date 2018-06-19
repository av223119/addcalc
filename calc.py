import re

def add(numbers):
    del_spec = re.fullmatch(r"//\[(.)\]\n(.*)", numbers)
    sep = r"[,\n]"
    if del_spec:
        numbers = del_spec.group(2)
        sep = re.escape(del_spec.group(1))
    if numbers == "":
        return 0
    lst = [ int(x) for x in re.split(sep, numbers) if int(x) <= 1000 ]
    negatives = [ str(x) for x in lst if x < 0 ]
    if negatives:
        raise ValueError("negatives not allowed: {0}".format(",".join(negatives))) 
    return sum(lst)
