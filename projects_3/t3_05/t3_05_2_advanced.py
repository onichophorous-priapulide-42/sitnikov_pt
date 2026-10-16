sys = int(input())
dys = int(input())
if sys < 120 and dys < 80:
    print("оптимальное")
elif sys < 130 and dys < 85:
    print("нормальное")
elif sys < 140 and dys < 90:
    print("высокое нормальное")
else:
    print("гипертензия")