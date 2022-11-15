# 시간 초과 소스
import sys
N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    while (i > 0) & (grid[i][0] < grid[i-1][0]):
        grid[i], grid[i-1] = grid[i-1], grid[i]
        i -= 1
    while (i > 0) & (grid[i][0] == grid[i-1][0]) & (grid[i][1] < grid[i-1][1]):
        grid[i], grid[i-1] = grid[i-1], grid[i]
        i -= 1
print(grid)

# sort 사용 - nlogn
import sys
N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))
grid.sort(key=lambda x: (x[0], x[1]))  # 첫번째인자 x[0]부터 정렬 후, 두번째 인자 x[1] 정렬
for j in range(N):
    print(grid[j][0], grid[j][1])

# nlogn인 타정렬알고리즘
