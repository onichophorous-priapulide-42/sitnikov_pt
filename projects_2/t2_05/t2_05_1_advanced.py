dna = input()[::-1]
dna = dna.replace("A", "#").replace("T", "A").replace("#", "T")
dna = dna.replace("G", "#").replace("C", "G").replace("#", "C")
print(dna)