# 내 소스
n, m = map(int, input().split())
b = []

for i in range(n):
    a = list(map(int, input().split()))
    b.append(min(a))
print(max(b))