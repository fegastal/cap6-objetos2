seq = "TKKAMCRAATARKWC"
counts = {}
for letter in "ABCDGHKMNRSTUWY":
    counts[letter] = seq.count(letter)

prints(counts)

