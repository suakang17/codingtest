submitted = [int(input()) for i in range(28)]
for i in range(1,31):
    if i not in submitted:
        print(i)

# 타 소스 - 제출자 지워나가기
x=list(map(int,range(31)))
del x[0]
for i in range(28):
    x.remove(int(input()))
for j in x:
    print(j)

# 타 소스2 - 차집합 이용
import sys

a, b = set(range(1, 31)) - set(map(int, sys.stdin))
print(min(a, b))
print(max(a, b))