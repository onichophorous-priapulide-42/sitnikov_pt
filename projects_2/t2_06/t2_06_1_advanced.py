species = input().strip().lower()
jammed = species.split(" ")
jammed[0] = jammed[0][0].upper() + ". "
print("".join(jammed))