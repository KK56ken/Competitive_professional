def main():
    n = []
    for _ in range(3):
        n.append(input())
    
    if "ARC" in n:
        if "AGC" in n:
            if "AHC" in n:
                print("ABC")
            else:
                print("AHC")
        else:
            print("AGC")
    else:
        print("ARC")

main()
