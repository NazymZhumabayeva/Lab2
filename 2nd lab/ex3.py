def square_after_index(list, i):
    return list[:i] + [j * j for j in list[i:]]

print(square_after_index([10, 3, 4, 5, 9], 2))
