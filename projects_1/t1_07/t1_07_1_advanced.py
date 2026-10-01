import math

measured = 0.02
nominal = 0.0
percent = 1
floor = 0.05

print(math.isclose(measured, nominal, rel_tol=(percent/100), abs_tol = floor))
