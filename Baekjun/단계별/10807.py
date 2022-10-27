N = int(input())
N_list = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in N_list:
    if i == v:
        cnt += 1
print(cnt)

# 모범 소스
number = int(input())
a = map(int, input().split())
listA = list(a)
b = int(input())
print(listA.count(b))