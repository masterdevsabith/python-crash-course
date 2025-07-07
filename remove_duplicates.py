numbers = [10, 2, 5, 2, 2, 2, 4, 7, 7, 1, 10]
uniques = []

for n in numbers:
    if n not in uniques:
        uniques.append(n)

print(uniques)
