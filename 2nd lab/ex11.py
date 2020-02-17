def differences(a, b):
#    return a & b
    for i in b:
        if i in a:
            a.remove(i)
    return a

print(differences({1, 2, 3, 4}, {3, 5, 7}))