# 내 소스 ======================================오답
n, m = map(int, input().split())
a, b, d = map(int, input().split())

location = []
count = 1  # 처음 위치 포함
d_type = [0, 1, 2, 3]  # 북 동 남 서
da = [-1, 0, 1, 0]  # a좌표 기준 이동벡터 북 동 남 서
db = [0, 1, 0, -1]  # b좌표 기준 이동벡터 북 동 남 서

for i in range(n):  # n줄 입력
    location.append([])
    for j in location:
        j.append(input().split())  # 2중 리스트 형성

# 시뮬레이션 시작
for direction in d_type:  # 매뉴얼 1
    if d_type[direction] == d:  # 현재 바라보는 방향 파악(기준점-이 기준으로 반시계로 갈 수 있는지 여부 확인)
        for i in d_type:  # 매뉴얼 2
            na = a + da[d_type[direction - i]]
            nb = b + db[d_type[direction - i]]
            if location[na][nb] != 1:  # 앞으로 갈 수 있는 경우
                location[na][nb] = 1  # 가본 칸은 현재부로 바다로 취급 (가지 않도록)
                count += 1
                a = na  # 현위치 변경
                b = nb
                d = d_type[direction - i]  # d값 변경
                break  # d값이 변경되었으므로 바깥 for문부터 다시 돌도록
            else:  # 앞으로 갈 수 없는 경우
                continue
    else:
        continue

for direction in d_type:
    if d_type[direction] == d:  # 현재 바라보는 방향 파악(기준점-이 기준으로 반시계로 갈 수 있는지 여부 확인)
        for i in d_type:  # 네 방향 모두 갈 수 없는 칸인 경우
            na = a - da[d_type[direction - i]]
            nb = b - db[d_type[direction - i]]
            if location[na][nb] != 1:  # 뒤로 갈 수 있는 경우
                location[na][nb] = 1  # 가본 칸은 앞으로 바다로 취급 (가지 않도록)
                count += 1
                a = na  # 현위치 변경
                b = nb
                continue
            else:  # 뒤로도 못 가는 경우
                break
        break
print(count)

# =============================================모범 소스
n, m = map(int, input().split())

# 방문한 칸 저장 위한 맵 d 생성, 초기화(0)  # 내 소스에서는 입력받은 맵인 location 하나로 사용, 여기서는 방문기록과 지형지도를 분리
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())  # 내 소스 a, b, d
d[x][y] = 1  # 초기 위치 방문했음으로 처리

# 전체 맵 정보 input
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서- 내 소스 da, db
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# turn_left 함수
def turn_left():  # 내 소스에서는 turn_left() 구현하는 대신 인덱스를 direction-i로 둠
    global direction
    direction -= 1
    if direction == -1:
        direction = 3  # direction의 값은 0,1,2,3 뿐이므로


# 시뮬레이션 시작
count = 1
turn_time = 0  # 네 방향 모두 1인 경우 케이싱 위함

while True:
    turn_left()  # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 회전 후 정면에 가보지 않은 칸 존재시 이동
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:  # 회전 후 정면 칸에 방문 불가
        turn_time += 1
    if turn_time == 4:  # 네 방향 모두 방문 불가
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:  # 뒤로 갈 수 있는 경우
            x = nx
            y = ny
        else:  # 뒤로도 못 가는 경우
            break
        turn_time = 0

print(count)
