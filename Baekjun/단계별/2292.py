n = int(input())
k = 1
while True:
    if n == 1:
        print(1)
        break
    elif n <= 1 + 6*int((k*(k+1))//2):
        print(k+1)
        break
    else:
        k += 1

# 벌집개수 층별: 1개 6개 12 18 ...
# 1
# 1+6
# 1+6+12
# 1+6+12+18

# 타 소스
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)