dna = input()
motive = input()
l = len(motive)

start = dna.find(motive)
finish = dna.rfind(motive)

print(dna[start + l:finish])