seq = "TKKAMCRAATARKWC"
counts = {}
for base in seq:
    if base not in counts:
        n = 0
    else:
        n = counts[base]
    counts[base] = n + 1

prints(counts)

