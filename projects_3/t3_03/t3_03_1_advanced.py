dna = input()
ceil = float(input())/100
print(dna != "" and (dna.count("G") + dna.count("C"))/len(dna) > ceil)