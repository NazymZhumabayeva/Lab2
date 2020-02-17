def power(s):
    t = set()
    for i in s:
        x = i
        while(x in s):
            x *= i
        t.add(x)
    return t

print(power([1, 2, 2, 3, 4])