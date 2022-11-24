
n = int(input("n칸 입력 >> "))
# di = ["R"] #,"R","R","U","D","D"]
di = list(map(str, input("방향 입력 >> ").split()))

# 초기 값 
x, y = 1, 1 # 1,1 시작

move_type = ['L','R','U','D']
dx = [-1, 1, 0, 0] # x축 이동
dy = [0,0,-1, 1] # y축 이동

for inp in di:
    # move_type.index(p) # 인덱스 값 출력받기
    direction = move_type.index(inp) # 방향
    cx = x + dy[direction]
    cy = y + dx[direction]

    if any([cx < 1, cy < 1, cx > n, cy > n]): # == or
        #1보다 작거나 n을 초과할 때
        continue
    else:
        x, y = cx, cy

print(x, y)

li = [ [0,0,0,0,0] for i in range(5) ]
li[cx-1][cy-1] = 1

for i in range(5):
    print(li[i])