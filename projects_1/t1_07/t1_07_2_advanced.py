import math

c0 = 0.5
k = 10
n = 3
target = 0.0005
result = c0/(k**n)
percent = 10**-6

print(math.isclose(result, target, rel_tol=percent))
