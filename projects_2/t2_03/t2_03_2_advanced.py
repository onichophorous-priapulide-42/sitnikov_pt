dna = input()
start = int(input()) - 1
finish = int(input())
print(dna[:start] + dna[start:finish] * 2 + dna[finish:])