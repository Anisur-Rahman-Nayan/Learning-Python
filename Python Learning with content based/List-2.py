alphabet = ["A","B","C","D","E","F","G","H","I","J"]

print(len(alphabet))

alphabet.append("K")
print(alphabet)

alphabet.insert(2,"X")
print(alphabet)

alphabet.remove("X")
print(alphabet)

alphabet.sort()
print(alphabet)

alphabet.reverse()
print(alphabet)

alphabet.pop()
print(alphabet)

#alphabet.clear()

alphabet2 = alphabet.copy()
print(alphabet2)

position = alphabet.index("F")
print(position)

count = alphabet.count("C")
print(count)

