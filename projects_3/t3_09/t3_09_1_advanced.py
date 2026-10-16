dna = input()
if not dna:
    print("пустая")
elif dna.upper().replace("A", "").replace("C", "").replace("G", "").replace("T", "").replace("N", ""):
    print("недопустимые символы")
elif (dna.count("N") + dna.count("n")) > len(dna)/2:
    print("низкое качество")
elif dna.lower() == dna:
    print("замаскирована")
else:
    print("OK")