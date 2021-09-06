def main():
    n = int(input())

    names = []

    for i in range(n):
        name = {}
        sei,mei = input().split()
        name["sei"] = sei
        name["mei"] = mei
        names.append(name)
        
    if check(names,n):
        print("Yes")
    else:
        print("No")


def check(names,n):
    for i in range(n-1):
        for j in range(1,n-i):
            if names[i]["sei"] == names[j+i]["sei"]:
                if names[i]["mei"] == names[j+i]["mei"]:
                    return True
    return False

main()
