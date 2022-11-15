import sys
N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(int, sys.stdin.readline().strip().split())))
grid.sort(key=lambda x: (x[1], x[0]))
for j in range(N):
    print(grid[j][0], grid[j][1])