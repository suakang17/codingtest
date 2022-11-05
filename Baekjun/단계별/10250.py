# 틀린 소스  (1 5 4 반례)
# import sys
# T = int(sys.stdin.readline().strip())
# for i in range(T):
#     H, W, N = map(int, sys.stdin.readline().strip().split())  # 층수, 방수, 몇번째 손님인지
#     if N % H != 0:
#         floor = N % H
#     else:  # 나누어 떨어지는 경우 처리 필요
#         floor = H
#     if (N/H) <= 1:
#         roomnum = 1
#         print(floor*100 + roomnum)
#     else:
#         roomnum = int(N//H) + 1
#         print(floor*100 + roomnum)

# 정답 소스
import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split())  # 층수, 방수, 몇번째 손님인지
    if N % H != 0:
        floor = N % H * 100
        roomnum = 1 + (N//H)
    else:  # 나누어 떨어지는 경우 처리 필요
        floor = H * 100
        roomnum = N//H
    print(floor+roomnum)