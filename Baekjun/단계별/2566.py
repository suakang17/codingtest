# 틀린 소스 - 입력 81개가 모두 0인 경우 max_i, max_j ==0 으로 초기화 되어있기 때문에 0 0 0이 출력되는데, 주어진 행렬은 1, 1부터 시작하므로 답은 0, 1,1 으로 출력되도록 수정해야함
# 이유: 반례 고려 못함
import sys
l = [sys.stdin.readline().strip().split() for i in range(9)]
max = 0
max_i = 0
max_j = 0
for i in range(9):
    for j in range(9):
        l[i][j] = int(l[i][j])
        if l[i][j] > max:
            max = l[i][j]
            max_i = i + 1
            max_j = j + 1
print(max)
print(max_i, max_j)

# 정답 소스
import sys
l = []
for _ in range(9):
    l.append(list(map(int, sys.stdin.readline().split())))
max = 0
max_i = 1
max_j = 1
for i in range(9):
    for j in range(9):
        if l[i][j] > max:
            max = l[i][j]
            max_i = i + 1
            max_j = j + 1
print(max)
print(max_i, max_j)

