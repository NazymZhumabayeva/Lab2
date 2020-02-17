def more_than_given(a, n):
    s = set()
    for j in a:
        if j > n:
            s.add(j)
    return s

print(more_than_given([11,2,44,23], 10))