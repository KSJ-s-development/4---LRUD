# pos = input()
pos = 'a1'
col = ord(pos[0]) - 96
row = int(pos[1])

# 이동가능한 경우의 수 - 총8
move_case = [
    (-2,-1),(-2, 1),
    (-1,-2),(-1, 2),
    (1,-2),(1, 2),
    (2,-1),(2, 1),
]
#경우의 수
result = 0

#비교
for m in move_case:
    move_col = col + m[0]
    move_row = row + m[1]

    # 만족한 경우만 True반환
    cheesboard = all([move_col >=1, move_col<=8,
                    move_row >=1, move_row<=8])
    if cheesboard :
        result +=1

print(f"경우의 수 : {result}")