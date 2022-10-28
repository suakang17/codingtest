# 색종이가 도화지 밖으로 나가는 경우가 없으니 인덱스 오버플로우는 고려하지 않는다.
import sys
n = int(input())
area = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            area[a+i][b+j] = 1

cnt = 0
for row in area:
    cnt += row.count(1)
print(cnt)