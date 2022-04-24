def main():
    N = int(input())
    S = input()
    Coordinate = [0,0]
    
    direction = 0
    
    for i in range(N):
        if S[i] == "S":
            if direction == 0:
                Coordinate[0] += 1
            elif direction == 1:
                Coordinate[1] -= 1
            elif direction == 2:
                Coordinate[0] -= 1
            elif direction == 3:
                Coordinate[1] += 1
        elif S[i] == "R":
            if direction == 3:
                direction = 0
            else:
                direction += 1
    print(Coordinate[0],Coordinate[1])

main()