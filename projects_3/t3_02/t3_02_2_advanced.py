first = input()
second = input()
pur = ["A", "G"]
pyr = ["T", "C"]
print((first in pur and second in pur and first != second) or (first in pyr and second in pyr and first != second))