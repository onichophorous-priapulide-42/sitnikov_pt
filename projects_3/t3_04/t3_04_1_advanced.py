start = int(input())
finish = int(input())

if input() == "+".strip():
    p = int(input())
    print(p - start + 1)
else:
    p = int(input())
    print(-p + finish + 1)
