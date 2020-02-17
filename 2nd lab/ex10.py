def neighbors(set_):
    s = set()
    for i in set_:
        s.add(i - 1)
        s.add(i + 1)
    return s

print(neighbors({1, 5, 9}))