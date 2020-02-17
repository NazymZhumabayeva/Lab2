def number(a):
    cnt = 0
    for i in a[0::2]:
        if a%2==1:
            cnt += 1
    return cnt

print(number([0,3,11,2,44,23,4]))