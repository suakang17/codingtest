count = 1  # 초기 위치 포함
n, m = map(int, input().split())
x, y, d = map(int, input().split())  # 초기위치, 바라보고 있는 방향
board = []
for i in range(n):
    board.append(list(int(input().split())))  # [column][row]로 접근
d_type = [0, 1, 2, 3]  # 바라보고 있는 방향 (북동남서)
front_type = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 앞으로 한 칸 (북동남서)
back_type = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # 뒤로 한 칸 (북동남서)

while True:
    for i in d_type:
        if i != d:
            continue
        dx = x + front_type[i-1][0]
        dy = y + front_type[i-1][1]
        if board[dx][dy] == 1 or dx < 0 or dx > n or dy < 0 or dy > m:  # 가려는 칸이 바다인 경우
            continue