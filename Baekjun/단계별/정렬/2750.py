# 내 소스 (버블) O(n²)
import sys

N = int(sys.stdin.readline().strip())
l = []
for i in range(N):
    l.append(int(sys.stdin.readline().strip()))
num = 0
for j in range(len(l)-1):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            num = l[i]
            l[i] = l[i + 1]
            l[i + 1] = num
for k in range(len(l)):
    print(l[k])

# 모범 소스 1 - 내장함수 sort
import sys

N = int(sys.stdin.readline().strip())
l = []
for i in range(N):
    l.append(int(sys.stdin.readline().strip()))
l.sort()
for i in l:
    print(i)

# 모범 소스 2 - 버블정렬 (내풀이 개선 ver.)
N = int(input())

num = []

for _ in range(N):
    num.append(int(input()))       # 표준입력은 sys사용이 더 올바를듯

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

for n in num:
    print(n)

# 모범 소스 3 - 삽입정렬
N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

for i in range(1, len(num)):
    while (i > 0) & (num[i] < num[i-1]):
        num[i], num[i-1] = num[i-1], num[i]
        i -= 1

for n in num:
    print(n)

# 숏코딩
[print(v) for v in sorted([int(input()) for _ in range(int(input()))])]