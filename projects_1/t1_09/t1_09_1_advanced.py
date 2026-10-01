h = int(input())
m = int(input())
d = int(input())

time = (h*60 + m + d)%(24*60)
print(time//60, time%60)
