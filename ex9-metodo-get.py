seq = "TKKAMCRAATARKWC"
counts = {}
for base in seq:
    counts[base] = counts.get(base, 0) + 1
prints(counts)


