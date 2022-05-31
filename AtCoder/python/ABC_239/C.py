import math

def main():
    offset = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
    
    x1,y1,x2,y2 = map(int,input().split())
    flag1 = False
    flag2 = False
    
    
    root5 = math.sqrt(5)
    print(root5)
    for i in range(len(offset)):
        result1 = math.sqrt(((x1 - offset[i][0]) ** 2) + ((y1 - offset[i][1]) ** 2))
        print(((x1 - offset[i][0]) ** 2) + ((y1 - offset[i][1]) ** 2))
        result2 = math.sqrt(((x2 - offset[i][0]) ** 2) + ((y2 - offset[i][1]) ** 2))
        print(result1,result2)
        
        if root5 == result1:
            flag1 = True
            
        if root5 == result2:
            flag2 =True
        if flag1 and flag2:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()