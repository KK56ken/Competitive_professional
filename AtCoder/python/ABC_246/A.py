def main():
    listx = []
    listy = []
    
    for _ in range(3):
        x,y = map(int,input().split())
        listx.append(x)
        listy.append(y)
        
    print(*[x for x in set(listx) if listx.count(x) == 1],*[x for x in set(listy) if listy.count(x) == 1])

main()