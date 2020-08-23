
mozi = input()
a = list(mozi)
if a[0] == 'R' and a[1] == 'R' and a[2] == 'R':
    print(3)
elif a[0] == 'R' and a[1] == 'R':
    print(2)
elif a[1] == 'R' and a[2] == 'R':
    print(2)
elif a[0] == 'R':
    print(1)
elif a[1] == 'R':
    print(1)
elif a[2] == 'R':
    print(1)
else:
    print(0)
