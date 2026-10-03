gc = int(input())
num = gc // 5
print(f'[{num * "   #" + (20 - num) * "."}] {gc:>3}%')