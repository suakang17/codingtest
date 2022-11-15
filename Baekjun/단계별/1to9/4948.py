# 시간 초과
# import sys
# while True:
#     n = int(sys.stdin.readline().strip())
#     if n == 0:
#         break
#     cnt = 0
#     if n == 1:
#         print(1)
#         continue
#     for i in range(n+1, 2*n+1):
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 break
#             if j == int(i**0.5):
#                 cnt += 1
#     print(cnt)

# 정답 소스 - 미리 판별해두고 일치여부 확인
def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True


value = list(range(1, 123456*2+1))
prime_num = []

for i in value:
    if is_prime(i):  # return값이 True이면
        prime_num.append(i)

import sys
while True:
    inputnum = int(sys.stdin.readline().strip())
    if inputnum == 0:
        break
    cnt = 0
    for k in prime_num:
        if inputnum < k <= inputnum*2:
            cnt += 1
    print(cnt)