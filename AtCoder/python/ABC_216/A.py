x = str(input())
y = int(x[-1])
if y >= 0 and y <= 2:
    print(str(float(x))[0:len(x)-2]+"-")
elif y >= 3 and y <= 6:
    print(str(float(x))[0:len(x)-2])
elif y >= 7 and y <= 9:
    print(str(float(x))[0:len(x)-2]+"+")
