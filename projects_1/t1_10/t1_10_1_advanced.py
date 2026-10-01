length = int(input())
g = int(input())
c = int(input())
n = int(input())

known = length - n

print(f'{100*(g+c)/known:0.1f}')
