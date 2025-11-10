import itertools


# Itertools examples: Te permite trabajar sin crear estructuras intermedias y 
# combinando flujos de datos de forma perezosa (lazy evaluation).

data = [1, 2, 3, 4]

print(list(itertools.accumulate(data)))     # [1, 3, 6, 10]
print(list(itertools.permutations("ABC")))  # [('A','B','C'), ...]
print(list(itertools.islice(range(100), 10, 15)))  # [10, 11, 12, 13, 14]
print(list(itertools.chain("ABC", "DEF")))  # ['A', 'B', 'C', 'D', 'E', 'F']
print(list(itertools.compress("ABCDE", [1, 0, 1, 0, 1])))  # ['A', 'C', 'E']