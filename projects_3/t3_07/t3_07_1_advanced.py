ceil = float(input())
n0 = float(input() or -1)
n1 = float(input() or -1)
n2 = float(input() or -1)
if n0 > ceil:
    print(0)
elif n1 > ceil:
    print(1)
elif n2 < ceil:
    print(2)
else:
    print("нет сигнала")