def is_it_mutable(listik):
    for i in listik:
        if type(i) == list or type(i) == dict or type(i) == set:
            return True
    return False

print(is_it_mutable((10, 2, 5, [4, 8, 2], 3, 5)))