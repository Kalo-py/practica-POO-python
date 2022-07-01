lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()

#Son los paréntesis. Los corchetes hacen una comprensión, los paréntesis hacen un generador.
#