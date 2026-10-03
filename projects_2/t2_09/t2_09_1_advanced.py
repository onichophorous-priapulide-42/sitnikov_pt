info = input().split(" ")[0][1:]
dna = input().lower()
dna3 = dna[2::3]
l = len(dna)
l3 = len(dna3)
gc = 100 * (dna.count("g") + dna.count("c")) / l
gc3 = 100 * (dna3.count("g") + dna3.count("c")) / l3
print(f'{info}	{l}	{gc:.1f}	{gc3:.1f}')