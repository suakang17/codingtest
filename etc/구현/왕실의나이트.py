# ====================================== 내 소스
input_data = input()
column = int(input_data[1])
row = ord(input_data[0])-ord('a') + 1  # 굳이 'A' 를 빼주어야? -> 후에 사용시에 골치 덜아픔
                                       # + 1은 행처럼 1~8의 값 갖게 하기 위함 (원래는 0~7)
count = 0
dc = [-1, 1]  # 상하
dr = [-1, 1]  # 좌우

# 수직 2칸 -> 수평 1칸 경우
for i in dc:  # 상하 2가지 경우 (0~1)
    nc = column + 2*i
    if nc < 1 or nc > 8:  # 범위 이탈
        continue
    for j in dr:
        nr = row + j
        if nr < 1 or nr > 8:  # 범위 이탈
            continue
        else:
            count += 1
# 수평 2칸 -> 수직 1칸 경우
for m in dr:  # 좌우 4가지 경우 (0~1)
    nr = row + 2*m
    if nr < 1 or nr > 8:  # 범위 이탈
        continue
    for n in dc:
        nc = column + n
        if nc < 1 or nc > 8:  # 범위 이탈
            continue
        else:
            count += 1
print(count)

# ====================================== 모범 소스
input_data = input()
column = int(input_data[1])
row = ord(input_data[0])-ord('a') + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)