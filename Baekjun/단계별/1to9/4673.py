n = 0
selfnum = set(k for k in range(1, 10000))

for num in range(1, 10001):  # 숫자 자기 자신 (주어진 수)
    for i in str(num):
        num += int(i)  # 자기 자신 + 자릿수
    selfnum.discard(num)

for sn in selfnum:
    print(sn)

# append 사용하는 경우도 O