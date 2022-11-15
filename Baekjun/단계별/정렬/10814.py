import sys
N = int(input())
l = []
for i in range(N):
    l.append(list(sys.stdin.readline().strip().split()))  # 인덱스 == 가입한순서
    l[i][0] = int(l[i][0])  # 나이 int로 수정
l.sort(key=lambda x: x[0])
for i in range(len(l)):
    print(l[i][0], l[i][1])