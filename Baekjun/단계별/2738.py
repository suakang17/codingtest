import sys
n, m = map(int, input().split())
a_list = []
b_list = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().strip().split()))  # sys.stdin.read().splitlines()로 대체가능, 줄 단위로 잘라 리스트로 저장
    a_list.append(a)
for j in range(n):
    b = list(map(int, sys.stdin.readline().strip().split()))
    b_list.append(b)

for i in range(n):
    for j in range(m):
        print(a_list[i][j]+b_list[i][j], end=' ')
    print()

# 타 소스
